"""Preview discovery must not pretend that an unimplemented host can execute."""
import json
from pathlib import Path

from danceflow_agents.ecosystem import EcosystemBridge
from danceflow_agents.discovery import DiscoveryIndex


def test_preview_discovery_exposes_references_and_host_limits_without_execution():
    hub = EcosystemBridge(None)
    try:
        index = DiscoveryIndex(hub.catalogue, hub.capabilities()['components'], [])
        for name, query in [('potbot', 'Potbot'), ('danceflow-unity', 'Unity')]:
            row = hub.component(name)
            assert row['experimental'] is True
            assert row['runtime']['status'] == 'native_host_required'
            assert row['runtime']['qualification'] == 'source_preview'
            assert row['operations'] == []
            assert row['native_host_routes']
            results = index.search(query=query, kind='component', limit=100)
            assert name in {item['id'] for item in results['results']}
            assert 'planned' in hub.catalogue.read_component('potbot', 'guide').lower()
            assert 'acceptance' in hub.catalogue.read_component('danceflow-unity', 'guide').lower()
        assert 'potbot-unity' in {r['name'] for r in hub.catalogue.workflows()}
    finally:
        hub.close()
