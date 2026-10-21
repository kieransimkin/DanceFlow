"""Keep a canonical component MCP server alive using the official SDK client.

The client, its subprocess and its async context managers all belong to one
worker task. Requests never launch a second server or retry an uncertain call.
"""
from __future__ import annotations

import asyncio
from concurrent.futures import Future, InvalidStateError, TimeoutError as FutureTimeout
from pathlib import Path
import threading
from typing import Any


class NativeMCP:
    def __init__(self, command: str, arguments: list[str], workspace: Path,
                 *, environment: dict[str, str] | None = None, timeout: float = 90):
        self.command = command
        self.arguments = list(arguments)
        self.workspace = workspace
        self.environment = environment
        self.timeout = timeout
        self._requests: asyncio.Queue | None = None
        self._ready: Future = Future()
        self._thread: threading.Thread | None = None
        self._lock = threading.Lock()
        self._tools_lock = threading.Lock()
        self._loop: asyncio.AbstractEventLoop | None = None
        self._cancel_scope: Any = None
        self._pending: set[Future] = set()
        self._closed = False
        self._failure: str | None = None
        self._tools: list[Any] | None = None
        self.instructions = ""
        self.server_info: dict = {}

    @staticmethod
    def _finish(result: Future, value: Any = None, error: Exception | None = None) -> None:
        try:
            if error is not None:
                result.set_exception(error)
            else:
                result.set_result(value)
        except InvalidStateError:
            pass  # Shutdown and a received response may race to complete one request.

    def _start(self) -> None:
        with self._lock:
            if self._closed:
                raise RuntimeError("Native MCP connection is closed; restart DanceFlow")
            if self._failure:
                raise RuntimeError(self._failure)
            if self._thread is None:
                self._thread = threading.Thread(target=self._worker, daemon=True,
                                                name="danceflow-native-mcp")
                self._thread.start()
        try:
            self._ready.result(timeout=self.timeout)
        except FutureTimeout as exc:
            self.close()
            raise RuntimeError("Native MCP initialization timed out; no operation was retried") from exc

    def _worker(self) -> None:
        failure = "Native MCP disconnected; restart after checking its runtime"
        try:
            asyncio.run(self._serve())
        except BaseException as exc:
            failure = f"Native MCP disconnected ({type(exc).__name__}); restart after checking its runtime"
        finally:
            with self._lock:
                if not self._closed:
                    self._failure = failure
                message = "Native MCP connection is closed" if self._closed else failure
                if not self._ready.done():
                    self._ready.set_exception(RuntimeError(message))
                pending = list(self._pending)
                self._pending.clear()
                self._loop = self._requests = self._cancel_scope = None
            for result in pending:
                self._finish(result, error=RuntimeError(message))

    async def _serve(self) -> None:
        import anyio
        from mcp import ClientSession, MCPError
        from mcp.client.stdio import StdioServerParameters, stdio_client
        from mcp.types import PaginatedRequestParams, REQUEST_TIMEOUT

        parameters = StdioServerParameters(command=self.command, args=self.arguments,
                                           cwd=str(self.workspace), env=self.environment)
        # Use the same AnyIO cancellation mechanism as the SDK. Native
        # asyncio Task.cancel() can bypass its shielded subprocess cleanup.
        with anyio.CancelScope() as cancel_scope:
            with self._lock:
                self._loop = asyncio.get_running_loop()
                self._requests = requests = asyncio.Queue()
                self._cancel_scope = cancel_scope
                closed = self._closed
            if closed:
                return
            async with stdio_client(parameters) as (reader, writer):
                async with ClientSession(reader, writer, read_timeout_seconds=self.timeout) as session:
                    initialized = await session.initialize()
                    self.instructions = initialized.instructions or ""
                    self.server_info = initialized.server_info.model_dump(by_alias=True)
                    with self._lock:
                        if not self._ready.done():
                            self._ready.set_result(True)
                    while True:
                        method, arguments, result = await requests.get()
                        with self._lock:
                            if self._closed or result.done():
                                continue
                            # Atomically distinguish a queued request, which its
                            # caller can still cancel, from an operation whose
                            # native outcome may already be committed.
                            if not result.set_running_or_notify_cancel():
                                continue
                        try:
                            if method == "tools":
                                found, cursor = [], None
                                for _ in range(50):
                                    page = await session.list_tools(params=PaginatedRequestParams(cursor=cursor))
                                    found.extend(page.tools)
                                    cursor = page.next_cursor
                                    if cursor is None:
                                        break
                                else:
                                    raise ValueError("Native tool pagination exceeded its bound")
                                value = found
                            elif method == "call":
                                value = await session.call_tool(arguments["name"], arguments["arguments"])
                            else:
                                raise ValueError("Unsupported native MCP operation")
                            self._finish(result, value=value)
                        except Exception as exc:
                            if method == "call" and isinstance(exc, MCPError) and exc.code == REQUEST_TIMEOUT:
                                exc = RuntimeError("Native MCP response timed out; outcome is unknown. Inspect existing jobs before retrying.")
                            self._finish(result, error=exc)

    def _request(self, method: str, arguments: dict) -> Any:
        self._start()
        result: Future = Future()
        with self._lock:
            if self._closed or self._failure or self._loop is None or self._requests is None:
                raise RuntimeError(self._failure or "Native MCP connection is closed")
            self._pending.add(result)
            try:
                self._loop.call_soon_threadsafe(self._requests.put_nowait, (method, arguments, result))
            except RuntimeError:
                self._pending.discard(result)
                raise RuntimeError("Native MCP disconnected before accepting the request") from None
        try:
            return result.result(timeout=self.timeout + 5)
        except FutureTimeout as exc:
            if result.cancel():
                # The worker has not claimed this queue entry. Leave it marked
                # cancelled so it cannot run after the caller's deadline.
                raise RuntimeError("Native MCP request timed out before dispatch; no native operation was invoked") from exc
            # The remote operation may still have committed. In particular, do
            # not start another subprocess or repeat a job-submission request.
            raise RuntimeError("Native MCP response timed out; outcome is unknown. Inspect existing jobs before retrying.") from exc
        finally:
            with self._lock:
                self._pending.discard(result)

    def tools(self) -> list:
        with self._tools_lock:
            with self._lock:
                if self._closed or self._failure:
                    raise RuntimeError(self._failure or "Native MCP connection is closed")
            if self._tools is None:
                tools = self._request("tools", {})
                names = [tool.name for tool in tools]
                if len(names) != len(set(names)) or any(not name.startswith("stemlab_") for name in names):
                    raise ValueError("Unexpected tool names from the canonical StemLab provider")
                self._tools = tools
            return list(self._tools)

    def call(self, name: str, arguments: dict):
        from jsonschema import Draft202012Validator

        definitions = {tool.name: tool for tool in self.tools()}
        if name not in definitions:
            raise ValueError("Unknown native component tool")
        Draft202012Validator(definitions[name].input_schema).validate(arguments)
        return self._request("call", {"name": name, "arguments": arguments})

    def close(self) -> None:
        with self._lock:
            self._closed = True
            if not self._ready.done():
                self._ready.set_exception(RuntimeError("Native MCP connection is closed"))
            loop, cancel_scope = self._loop, self._cancel_scope
            pending = list(self._pending)
        for result in pending:
            self._finish(result, error=RuntimeError("Native MCP connection is closed; inspect pending job outcomes"))
        if loop is not None and cancel_scope is not None:
            try:
                loop.call_soon_threadsafe(cancel_scope.cancel)
            except RuntimeError:
                pass  # The worker completed its cleanup between the snapshot and this call.
        if self._thread is not None:
            self._thread.join(timeout=10)
            if self._thread.is_alive():
                raise RuntimeError("Native MCP shutdown did not finish; inspect the owned provider process")
