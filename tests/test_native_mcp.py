"""Exercise a real synthetic stdio provider through the official MCP client."""
from concurrent.futures import ThreadPoolExecutor
import json
import os
from pathlib import Path
import sys
import time

from jsonschema import ValidationError
import pytest

from danceflow_agents.native_mcp import NativeMCP


PROVIDER = r'''
import asyncio
import json
import os
from pathlib import Path
import sys
from mcp.server import MCPServer
from mcp.types import CallToolResult, ImageContent, TextContent, ToolAnnotations

events = Path(sys.argv[1])
def event(name):
    with events.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps({"event": name, "pid": os.getpid()}) + "\n")

event("started")
state = {"count": 0}
server = MCPServer("Synthetic StemLab", version="fixture-1", instructions="Synthetic fixture only")

@server.tool(annotations=ToolAnnotations(read_only_hint=False, destructive_hint=False))
def stemlab_increment(amount: int = 1) -> dict[str, int]:
    """Advance a counter retained by this provider process."""
    event("increment")
    state["count"] += amount
    return dict(state)

@server.tool()
def stemlab_preview() -> CallToolResult:
    """Return native image and structured content without flattening it."""
    return CallToolResult(
        content=[TextContent(type="text", text="synthetic preview"),
                 ImageContent(type="image", mime_type="image/png", data="iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII=")],
        structured_content={"evidence": "synthetic", "count": state["count"]},
        is_error=False,
    )

@server.tool()
def stemlab_expected_error() -> CallToolResult:
    return CallToolResult(content=[TextContent(type="text", text="fixture failure")], is_error=True)

@server.tool()
async def stemlab_delayed(seconds: float = 30) -> dict[str, str]:
    event("delayed")
    await asyncio.sleep(seconds)
    return {"job": "synthetic-job"}

@server.tool()
def stemlab_disconnect() -> dict:
    event("disconnect")
    os._exit(17)

server.run()
'''


def events_at(path):
    return [json.loads(line) for line in path.read_text("utf-8").splitlines()] if path.exists() else []


def wait_for_event(path, name, timeout=10):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        found = [entry for entry in events_at(path) if entry["event"] == name]
        if found:
            return found
        time.sleep(0.02)
    pytest.fail(f"Synthetic provider did not record {name}")


@pytest.fixture
def native_provider(tmp_path):
    script = tmp_path / "provider.py"
    script.write_text(PROVIDER, encoding="utf-8")
    events = tmp_path / "events.jsonl"
    # Keep cold-import startup allowance aligned with the real stdio smoke test.
    client = NativeMCP(sys.executable, ["-u", str(script), str(events)], tmp_path, timeout=90)
    yield client, events
    client.close()


def test_native_schema_state_and_multimodal_result_are_preserved(native_provider):
    client, events = native_provider
    tools = {tool.name: tool for tool in client.tools()}
    increment = tools["stemlab_increment"]
    assert increment.input_schema["properties"]["amount"]["type"] == "integer"
    assert increment.annotations.read_only_hint is False
    assert client.instructions == "Synthetic fixture only"
    assert client.server_info["version"] == "fixture-1"
    assert client.call("stemlab_increment", {"amount": 2}).structured_content == {"count": 2}
    assert client.call("stemlab_increment", {"amount": 3}).structured_content == {"count": 5}
    preview = client.call("stemlab_preview", {})
    assert [item.type for item in preview.content] == ["text", "image"]
    assert preview.content[1].mime_type == "image/png"
    assert preview.content[1].data.startswith("iVBOR")
    assert preview.structured_content == {"evidence": "synthetic", "count": 5}
    error = client.call("stemlab_expected_error", {})
    assert error.is_error and error.content[0].text == "fixture failure"
    assert len([entry for entry in events_at(events) if entry["event"] == "started"]) == 1


def test_concurrent_native_calls_share_one_provider_and_state(native_provider):
    client, events = native_provider
    with ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(lambda _: client.call("stemlab_increment", {}), range(12)))
    assert sorted(result.structured_content["count"] for result in results) == list(range(1, 13))
    recorded = events_at(events)
    assert sum(entry["event"] == "started" for entry in recorded) == 1
    assert sum(entry["event"] == "increment" for entry in recorded) == 12


def test_native_arguments_are_checked_before_invocation(native_provider):
    client, events = native_provider
    with pytest.raises(ValidationError):
        client.call("stemlab_increment", {"amount": "invalid"})
    with pytest.raises(ValueError, match="Unknown"):
        client.call("unregistered_tool", {})
    assert not any(entry["event"] == "increment" for entry in events_at(events))


def test_uncertain_native_call_is_never_retried(native_provider):
    client, events = native_provider
    client.tools()
    # Apply a short caller deadline after the potentially slow cold startup.
    client.timeout = 0.01
    with pytest.raises(RuntimeError, match="outcome is unknown"):
        client.call("stemlab_delayed", {"seconds": 30})
    recorded = events_at(events)
    assert sum(entry["event"] == "delayed" for entry in recorded) == 1
    assert sum(entry["event"] == "started" for entry in recorded) == 1


def test_queued_native_call_expired_before_dispatch_is_not_invoked(native_provider):
    client, events = native_provider
    client.tools()
    with ThreadPoolExecutor(max_workers=1) as pool:
        active = pool.submit(client.call, "stemlab_delayed", {"seconds": 6})
        wait_for_event(events, "delayed")
        # The active request already has its ordinary deadline. Only the new
        # queued request gets the shorter caller deadline (plus its five-second
        # response allowance), so it expires before the provider can accept it.
        client.timeout = 0.01
        with pytest.raises(RuntimeError) as timed_out:
            client.call("stemlab_increment", {})
        assert active.result(timeout=10).structured_content == {"job": "synthetic-job"}
    # A following response is also a queue barrier: the expired request had
    # every opportunity to run by this point if it was not cancelled.
    assert client.call("stemlab_preview", {}).structured_content["count"] == 0
    assert not any(entry["event"] == "increment" for entry in events_at(events))
    assert "before dispatch" in str(timed_out.value)
    assert client.call("stemlab_increment", {}).structured_content == {"count": 1}
    assert sum(entry["event"] == "started" for entry in events_at(events)) == 1


def test_close_cancels_active_and_queued_requests_and_reaps_provider(native_provider):
    client, events = native_provider
    client.tools()
    with ThreadPoolExecutor(max_workers=2) as pool:
        active = pool.submit(client.call, "stemlab_delayed", {"seconds": 30})
        wait_for_event(events, "delayed")
        queued = pool.submit(client.call, "stemlab_increment", {})
        client.close()
        for result in (active, queued):
            with pytest.raises(RuntimeError, match="closed"):
                result.result(timeout=2)
    assert client._thread is not None and not client._thread.is_alive()
    assert not any(entry["event"] == "increment" for entry in events_at(events))
    with pytest.raises(RuntimeError, match="closed"):
        client.tools()
    if os.name != "nt":
        pid = events_at(events)[0]["pid"]
        with pytest.raises(ProcessLookupError):
            os.kill(pid, 0)


def test_disconnected_native_provider_is_not_relaunched(native_provider):
    client, events = native_provider
    client.tools()
    with pytest.raises(Exception):
        client.call("stemlab_disconnect", {})
    with pytest.raises(Exception):
        client.call("stemlab_increment", {})
    assert sum(entry["event"] == "started" for entry in events_at(events)) == 1
    assert not any(entry["event"] == "increment" for entry in events_at(events))


def test_close_before_start_never_launches_a_provider(native_provider):
    client, events = native_provider
    client.close()
    with pytest.raises(RuntimeError, match="closed"):
        client.tools()
    assert not events.exists()
