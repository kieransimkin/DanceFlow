import pytest
from danceflow_agents.bridge import DanceFlowBridge


def test_analysis_delegates_and_cannot_download(tmp_path, monkeypatch):
    (tmp_path/'cover.png').write_bytes(b'synthetic protocol input')
    bridge=DanceFlowBridge(tmp_path)
    calls=[]
    monkeypatch.setattr(bridge, 'pixelcue_health', lambda: {'visual_analysis': {'route':'/v1/analysis'}})
    def request(route, payload, **options):
        calls.append((route,payload))
        return {'schema':'pixelcue.visual-analysis/1','fixture':True}
    monkeypatch.setattr(bridge,'_request',request)
    assert bridge.pixelcue_visual_analysis('cover.png')['fixture']
    assert calls[0][0]=='/v1/analysis'
    assert calls[0][1]['allow_download'] is False
    with pytest.raises(ValueError,match='Confirm'):
        bridge.pixelcue_visual_analysis('cover.png',['clip'])
    assert bridge.pixelcue_visual_analysis('cover.png',['clip'],True)['fixture']
    with pytest.raises(ValueError,match='Select'):
        bridge.pixelcue_visual_analysis('cover.png',['unknown'],True)


def test_old_service_and_bad_receipt_fail_explicitly(tmp_path, monkeypatch):
    (tmp_path/'cover.png').write_bytes(b'fixture')
    bridge=DanceFlowBridge(tmp_path)
    monkeypatch.setattr(bridge,'pixelcue_health',lambda:{})
    with pytest.raises(ValueError,match='0.9.0'):
        bridge.pixelcue_visual_analysis('cover.png')
    monkeypatch.setattr(bridge,'pixelcue_health',lambda:{'visual_analysis':True})
    monkeypatch.setattr(bridge,'_request',lambda *a,**kw:{'schema':'other'})
    with pytest.raises(ValueError,match='unsupported'):
        bridge.pixelcue_visual_analysis('cover.png')
