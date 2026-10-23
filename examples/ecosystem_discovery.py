"""Discover both preview components without importing or starting their hosts."""
from danceflow_agents.ecosystem import EcosystemBridge

def main():
    hub = EcosystemBridge(None)
    try:
        for name in ("potbot", "danceflow-unity"):
            row = hub.component(name)
            assert row["runtime"]["status"] == "native_host_required"
            assert row["runtime"]["qualification"] == "source_preview"
            assert not row["operations"]
            for section in ("capabilities", "skill", "guide"):
                text = hub.catalogue.read_component(name, section)
                assert text.strip()
            print(name, row["runtime"]["status"], "three references readable; no host invoked")
    finally:
        hub.close()

if __name__ == "__main__":
    main()
