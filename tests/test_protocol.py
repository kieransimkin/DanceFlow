"""Exercise the real JSON-RPC stdio server, including an actual KeywordMoves call."""
import json
import os
from pathlib import Path
import queue
import subprocess
import sys
import threading


def test_actual_stdio_tools_and_rejection(tmp_path):
    (tmp_path / "source.txt").write_text("Rhythmic movement and local analysis.", encoding="utf-8")
    env = dict(os.environ)
    env['PYTHONPATH'] = str(Path(__file__).resolve().parents[1] / 'src')
    proc = subprocess.Popen([sys.executable, '-m', 'danceflow_agents.server', '--workspace', str(tmp_path)],
                            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            text=True, encoding='utf-8', env=env)
    messages, errors = queue.Queue(), []
    def read():
        for line in proc.stdout:
            messages.put(line)
    def read_error():
        errors.extend(proc.stderr.readlines())
    threading.Thread(target=read, daemon=True).start()
    threading.Thread(target=read_error, daemon=True).start()
    identifier = 0
    def request(method, params):
        nonlocal identifier
        identifier += 1
        proc.stdin.write(json.dumps({'jsonrpc':'2.0', 'id':identifier, 'method':method, 'params':params})+'\n')
        proc.stdin.flush()
        while True:
            try:
                value = json.loads(messages.get(timeout=25))
            except queue.Empty as exc:
                raise AssertionError('No stdio response: '+''.join(errors)) from exc
            if value.get('id') == identifier:
                assert 'error' not in value, value
                return value['result']
    try:
        initial = request('initialize', {'protocolVersion':'2025-11-25', 'capabilities':{}, 'clientInfo':{'name':'danceflow-test','version':'1'}})
        assert initial['serverInfo']['name'] == 'DanceFlow'
        proc.stdin.write('{"jsonrpc":"2.0","method":"notifications/initialized"}\n')
        proc.stdin.flush()
        tools = request('tools/list', {})['tools']
        assert {x['name'] for x in tools} == {'danceflow_capabilities', 'keywordmoves_run', 'pixelcue_health', 'pixelcue_keywords'}
        response = request('tools/call', {'name':'keywordmoves_run', 'arguments':{'plugin':'text-library','operation':'extract-literal','inputs':['source.txt']}})
        assert not response.get('isError'), response
        result = json.loads(next(x['text'] for x in response['content'] if x['type'] == 'text'))
        assert any(x['phrase'] == 'rhythmic movement' for x in result['keywords'])
        denied = request('tools/call', {'name':'keywordmoves_run', 'arguments':{'plugin':'semrush','operation':'related','inputs':['source.txt']}})
        assert denied['isError'] is True
    finally:
        proc.stdin.close()
        try:
            proc.wait(timeout=8)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait(timeout=5)
