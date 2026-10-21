"""Exercise the real JSON-RPC hub, local operations and native MCP federation."""
import asyncio
import hashlib
import json
import os
from pathlib import Path
import queue
import subprocess
import sys
import threading
import time


def test_actual_stdio_tools_and_rejection(tmp_path):
    (tmp_path / "source.txt").write_text("Rhythmic movement and local analysis.", encoding="utf-8")
    env = dict(os.environ)
    env['PYTHONPATH'] = str(Path(__file__).resolve().parents[1] / 'src')
    trusted = tmp_path / 'trusted-code'
    (trusted / 'tools').mkdir(parents=True)
    (trusted / 'tools/check_blogworthiness.py').write_text(
        'import json,sys\nprint(json.dumps({"valid":False,"scope":"synthetic adapter fixture"}),flush=True)\nsys.exit(1)\n',
        encoding='utf-8')
    (trusted / 'workflows').mkdir()
    workflow_path = trusted / 'workflows/newsletter-publish.md'
    workflow_path.write_text('# Newsletter publication review\n\nReview a newsletter draft and its source evidence before publication.\n', encoding='utf-8')
    (trusted / 'skills/campaign').mkdir(parents=True)
    (trusted / 'skills/campaign/SKILL.md').write_text(
        '---\nname: campaign\ndescription: Review campaign evidence.\n---\n# Campaign review\n\nSynthetic read-only recipe.\n', encoding='utf-8')
    configuration = tmp_path / 'runtime.json'
    configuration.write_text(json.dumps({'schema':'danceflow.runtimes.v1',
        'components':{'workflowmoves':{'source_root':str(trusted)}}}),encoding='utf-8')
    proc = subprocess.Popen([sys.executable, '-m', 'danceflow_agents.server', '--workspace', str(tmp_path),
                             '--runtime-config',str(configuration)],
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
                # SDK cold import on Windows storage can take >30 seconds.
                # Bound startup separately; keep every initialized request's
                # original 25-second response deadline and all assertions.
                value = json.loads(messages.get(timeout=90 if method == 'initialize' else 25))
            except queue.Empty as exc:
                raise AssertionError('No stdio response: '+''.join(errors)) from exc
            if value.get('id') == identifier:
                assert 'error' not in value, value
                return value['result']
    try:
        initial = request('initialize', {'protocolVersion':'2025-11-25', 'capabilities':{}, 'clientInfo':{'name':'danceflow-test','version':'1'}})
        assert initial['serverInfo']['name'] == 'DanceFlow'
        assert 'danceflow_search' in initial['instructions']
        assert 'danceflow_list_workflows' in initial['instructions']
        proc.stdin.write('{"jsonrpc":"2.0","method":"notifications/initialized"}\n')
        proc.stdin.flush()
        tools = request('tools/list', {})['tools']
        names = {x['name'] for x in tools}
        assert len(names) == len(tools)
        assert {'danceflow_capabilities', 'keywordmoves_run', 'pixelcue_health', 'pixelcue_keywords',
                'pixelcue_visual_analysis','framerudiments_plan','likenessforge_train_lora',
                'workflowmoves_wordpress_schedule_post','dancerudiments_sample',
                'react_timeline_sequence_sample_beat_clock', 'danceflow_search',
                'danceflow_list_workflows', 'danceflow_get_workflow'} <= names
        for name in ('danceflow_search', 'danceflow_list_workflows', 'danceflow_get_workflow'):
            assert next(tool for tool in tools if tool['name'] == name)['annotations']['readOnlyHint'] is True
        search = next(tool for tool in tools if tool['name'] == 'danceflow_search')
        assert 'tool' in search['inputSchema']['properties']['kind']['enum']
        found = request('tools/call', {'name':'danceflow_search', 'arguments':{
            'query':'newsletter', 'kind':'workflow', 'component':'workflowmoves'}})
        assert not found.get('isError'), found
        match = next(row for row in found['structuredContent']['results']
                     if row['name'] == 'workflowmoves/workflows/newsletter-publish')
        # Follow the returned tool/arguments without constructing a resource URI.
        follow = match['next_call']
        procedure = request('tools/call', {'name':follow['tool'], 'arguments':follow['arguments']})
        assert not procedure.get('isError'), procedure
        procedure = procedure['structuredContent']
        assert procedure['content'] == workflow_path.read_bytes().decode('utf-8')
        assert procedure['source']['sha256'] == hashlib.sha256(workflow_path.read_bytes()).hexdigest()
        assert procedure['execution'] == 'instructions_only'
        page = request('tools/call', {'name':'danceflow_list_workflows', 'arguments':{'limit':3}})['structuredContent']
        workflow_names = [row['name'] for row in page['results']]
        total = page['total']
        assert page['coverage']['workflowmoves']['status'] == 'complete'
        while page['next_page'] is not None:
            follow = page['next_page']
            page = request('tools/call', {'name':follow['tool'], 'arguments':follow['arguments']})['structuredContent']
            workflow_names.extend(row['name'] for row in page['results'])
        assert len(workflow_names) == len(set(workflow_names)) == total
        assert {'framerudiments-complete', 'workflowmoves/skills/campaign'} <= set(workflow_names)
        discovered_tools = request('tools/call', {'name':'danceflow_search', 'arguments':{'kind':'tool','limit':100}})['structuredContent']
        assert {row['tool'] for row in discovered_tools['results']} == names
        assert discovered_tools['total'] == len(names)
        invalid = request('tools/call', {'name':'danceflow_search', 'arguments':{'limit':0}})
        assert invalid.get('isError') is True
        traversal = request('tools/call', {'name':'danceflow_get_workflow', 'arguments':{'name':'../../source.txt'}})
        assert traversal.get('isError') is True
        plan = next(x for x in tools if x['name']=='framerudiments_plan')
        assert plan['inputSchema']['properties']['arguments']['required']==['project','output']
        assert plan['inputSchema']['properties']['arguments']['additionalProperties'] is False
        assert plan['outputSchema']['type'] == 'object'
        assert plan['annotations']['destructiveHint'] is False
        publication = next(x for x in tools if x['name'] == 'workflowmoves_wordpress_schedule_post')
        assert publication['annotations']['destructiveHint'] is True
        assert publication['annotations']['openWorldHint'] is True
        inventory = request('tools/call', {'name':'danceflow_capabilities','arguments':{}})
        assert not inventory.get('isError'), inventory
        inventory = inventory['structuredContent']
        assert len(inventory['ecosystem']['components'])==15
        assert 'keywordmoves' in inventory and 'mcp_operations' in inventory
        templates=request('resources/templates/list',{})['resourceTemplates']
        assert 'danceflow://components/{name}/{section}' in {x['uriTemplate'] for x in templates}
        reference=request('resources/read',{'uri':'danceflow://components/mediaslide/skill'})
        assert 'MediaSlide' in reference['contents'][0]['text']
        prompt=request('prompts/get',{'name':'danceflow_workflow','arguments':{'component':'mediaslide','task':'Plan a media gallery'}})
        assert 'Plan a media gallery' in prompt['messages'][0]['content']['text']
        response = request('tools/call', {'name':'keywordmoves_run', 'arguments':{'plugin':'text-library','operation':'extract-literal','inputs':['source.txt']}})
        assert not response.get('isError'), response
        result = json.loads(next(x['text'] for x in response['content'] if x['type'] == 'text'))
        assert any(x['phrase'] == 'rhythmic movement' for x in result['keywords'])
        denied = request('tools/call', {'name':'keywordmoves_run', 'arguments':{'plugin':'semrush','operation':'related','inputs':['source.txt']}})
        assert denied['isError'] is True
        malformed=request('tools/call',{'name':'framerudiments_plan','arguments':{
            'arguments':{'project':'source.txt','output':'new-plan'},'permissions':{'write':'false'}}})
        assert malformed['isError'] is True
        job=request('tools/call',{'name':'workflowmoves_check_blogworthiness',
                                'arguments':{'arguments':{'path':'source.txt'}}})
        assert not job.get('isError'),job
        job_id=job['structuredContent']['job_id']
        deadline=time.monotonic()+15
        while True:
            state=request('tools/call',{'name':'danceflow_job_status','arguments':{'job_id':job_id}})['structuredContent']
            if state['status']!='running':break
            assert time.monotonic()<deadline
            time.sleep(.02)
        assert state['status']=='needs_review' and state['returncode']==1
        log=request('tools/call',{'name':'danceflow_job_logs','arguments':{'job_id':job_id}})['structuredContent']
        assert 'synthetic adapter fixture' in log['text']
    finally:
        proc.stdin.close()
        try:
            proc.wait(timeout=8)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait(timeout=5)


def test_native_tools_federate_through_the_actual_stdio_hub(tmp_path):
    """Check the hub's dispatch/result layer, beyond the native client in isolation."""
    from mcp import ClientSession
    from mcp.client.stdio import StdioServerParameters, stdio_client

    provider = tmp_path / "provider.py"
    provider.write_text('''
from mcp.server import MCPServer
from mcp.types import CallToolResult, ImageContent, TextContent, ToolAnnotations
server = MCPServer("Synthetic native provider")
state = {"count": 0}
@server.tool(annotations=ToolAnnotations(read_only_hint=False))
def stemlab_protocol_increment(amount: int = 1) -> dict[str, int]:
    state["count"] += amount
    return dict(state)
@server.tool()
def stemlab_protocol_preview() -> CallToolResult:
    return CallToolResult(content=[TextContent(type="text", text="synthetic"),
        ImageContent(type="image", mime_type="image/png",
                     data="iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII=")],
        structured_content={"count": state["count"]}, is_error=True)
server.run()
''', encoding="utf-8")
    launcher = tmp_path / "hub.py"
    launcher.write_text('''
from pathlib import Path
import sys
from danceflow_agents.bridge import DanceFlowBridge
from danceflow_agents.ecosystem import EcosystemBridge
from danceflow_agents.native_mcp import NativeMCP
from danceflow_agents.server import create_server
bridge = DanceFlowBridge(Path(sys.argv[1]))
ecosystem = EcosystemBridge(bridge.workspace)
ecosystem._native = NativeMCP(sys.executable, ["-u", sys.argv[2]], bridge.workspace)
create_server(bridge, ecosystem).run()
''', encoding="utf-8")
    env = dict(os.environ)
    env["PYTHONPATH"] = str(Path(__file__).resolve().parents[1] / "src")

    async def exercise():
        parameters = StdioServerParameters(command=sys.executable,
            args=["-u", str(launcher), str(tmp_path), str(provider)], env=env)
        async with stdio_client(parameters) as (reader, writer):
            async with ClientSession(reader, writer, read_timeout_seconds=90) as client:
                await client.initialize()
                tools = {tool.name: tool for tool in (await client.list_tools()).tools}
                native = tools["stemlab_protocol_increment"]
                assert native.input_schema["properties"]["amount"]["type"] == "integer"
                assert native.output_schema["additionalProperties"]["type"] == "integer"
                assert native.annotations.read_only_hint is False
                assert "keywordmoves_run" in tools
                found = await client.call_tool("danceflow_search", {"query":"stemlab_protocol_increment", "kind":"tool"})
                assert not found.is_error
                record = next(row for row in found.structured_content["results"]
                              if row["tool"] == "stemlab_protocol_increment")
                assert record["input_schema"] == native.input_schema
                assert record["output_schema"] == native.output_schema
                assert record["execution"] == "native_mcp"
                assert record["annotations"]["readOnlyHint"] is False
                first = await client.call_tool("stemlab_protocol_increment", {"amount": 2})
                second = await client.call_tool("stemlab_protocol_increment", {"amount": 3})
                assert first.structured_content == {"count": 2}
                assert second.structured_content == {"count": 5}
                result = await client.call_tool("stemlab_protocol_preview", {})
                assert result.structured_content == {"count": 5} and result.is_error
                assert [part.type for part in result.content] == ["text", "image"]
                assert result.content[1].mime_type == "image/png"
                assert result.content[1].data.startswith("iVBOR")

    asyncio.run(exercise())
