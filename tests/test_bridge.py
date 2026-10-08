import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread

import pytest

from danceflow_agents.bridge import DanceFlowBridge


def test_actual_keywordmoves_literal_evidence(tmp_path):
    (tmp_path / "sample.txt").write_text("Rhythmic movement. Rhythmic movement and musical timing.", encoding="utf-8")
    result = DanceFlowBridge(tmp_path).keyword_operation("text-library", "extract-literal", ["sample.txt"], {"limit": 12})
    assert result["plugin"] == "text-library"
    assert any(row["phrase"] == "rhythmic movement" for row in result["keywords"])
    assert all(row["evidence"][0]["metric"] == "occurrences" for row in result["keywords"])
    assert result["metadata"]


def test_workspace_escape_and_missing_configuration(tmp_path):
    work = tmp_path / "work"
    work.mkdir()
    (tmp_path / "private.txt").write_text("private", encoding="utf-8")
    with pytest.raises(ValueError, match="outside"):
        DanceFlowBridge(work)._file("../private.txt")
    with pytest.raises(ValueError, match="DANCEFLOW_WORKSPACE"):
        DanceFlowBridge(None)._file("private.txt")
    with pytest.raises(ValueError, match="individual file"):
        DanceFlowBridge(work)._file(".")


@pytest.mark.parametrize("url", ["https://example.com", "http://localhost:8765", "http://127.0.0.1:8765/path", "http://user@127.0.0.1:8765", "http://127.0.0.1:99999", "file:///tmp/media"])
def test_reject_non_loopback_or_ambiguous_endpoints(tmp_path, url):
    with pytest.raises(ValueError):
        DanceFlowBridge(tmp_path, url)


def test_limits_and_paid_provider_rejection(tmp_path):
    bridge = DanceFlowBridge(tmp_path)
    (tmp_path / "large.txt").write_bytes(b"a" * (1024 * 1024 + 1))
    with pytest.raises(ValueError, match="one-MiB"):
        bridge.keyword_operation("text-library", "extract-literal", ["large.txt"])
    with pytest.raises(ValueError, match="offline"):
        bridge.keyword_operation("semrush", "related", ["large.txt"])
    with pytest.raises(ValueError, match="Credentials"):
        bridge.keyword_operation("text-library", "extract-literal", ["large.txt"], {"llm": "openai"})
    with pytest.raises(ValueError, match="limit"):
        bridge.keyword_operation("text-library", "extract-literal", ["large.txt"], {"limit": 100000})


def test_actual_http_contract_and_inference_opt_in(tmp_path):
    received = []
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass
        def do_GET(self):
            assert self.path == "/health"
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps({"service": "pixelcue", "status": "ok", "models": ["smolvlm-256m"], "version": "fixture"}).encode())
        def do_POST(self):
            assert self.path == "/v1/keywords"
            received.append(json.loads(self.rfile.read(int(self.headers["Content-Length"]))))
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'["musical timing", "movement"]')
    http = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = Thread(target=http.serve_forever, daemon=True)
    thread.start()
    try:
        (tmp_path / "image.png").write_bytes(b"synthetic")
        bridge = DanceFlowBridge(tmp_path, f"http://127.0.0.1:{http.server_port}")
        with pytest.raises(ValueError, match="Confirm"):
            bridge.pixelcue_keywords("image.png")
        assert not received
        assert bridge.pixelcue_keywords("image.png", allow_inference=True) == ["musical timing", "movement"]
        assert received[0]["path"] == str((tmp_path / "image.png").resolve())
        assert received[0]["model"] == "smolvlm-256m"
    finally:
        http.shutdown()
        thread.join(timeout=3)
        http.server_close()
