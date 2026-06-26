"""End-to-end orchestration across environment data."""

from typing import Dict

from framework.record import Record
from .lifecycle import LifecycleTestSet


class E2ETestSet:
    """Run the lifecycle workflow and return an executive summary."""

    def __init__(self, record: Record, api_client, redfish_client, network_client, data):
        self.record = record
        self.lifecycle = LifecycleTestSet(record, api_client, redfish_client, network_client, data)
        self.data = data

    def run(self) -> Dict[str, object]:
        lifecycle_result = self.lifecycle.run()
        return {
            "environment": self.data.environment.name,
            "lifecycle": lifecycle_result,
            "summary": {
                "hosts_configured": len(lifecycle_result["hosts"]),
                "networks_configured": len(lifecycle_result["networks"]),
                "volumes_configured": len(lifecycle_result["volumes"]),
            },
        }
