"""End-to-end orchestration across environment data."""

from framework.record import Record
from metalshift.clients.api_client import APIClient
from metalshift.clients.network_client import NetworkClient
from metalshift.clients.redfish_client import RedfishClient
from metalshift.models.base import LifecycleData

from .lifecycle import LifecycleTestSet


class E2ETestSet:
    """Run the lifecycle workflow and return an executive summary."""

    def __init__(
        self,
        record: Record,
        api_client: APIClient,
        redfish_client: RedfishClient,
        network_client: NetworkClient,
        data: LifecycleData,
    ) -> None:
        self.record = record
        self.lifecycle = LifecycleTestSet(record, api_client, redfish_client, network_client, data)
        self.data = data

    def run(self) -> dict[str, object]:
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
