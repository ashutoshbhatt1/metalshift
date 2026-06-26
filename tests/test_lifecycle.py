import pytest

from metalshift.testsets.lifecycle import LifecycleTestSet


@pytest.mark.lifecycle
def test_lifecycle_configures_server_storage_bmc_and_network(
    lab_environment, api_client, redfish_client, network_client, test_record
):
    testset = LifecycleTestSet(test_record, api_client, redfish_client, network_client, lab_environment)
    result = testset.run()

    assert result["project"]["state"] == "active"
    assert result["hosts"][0]["state"] == "ready"
    assert result["bmc_sessions"][0]["session"].startswith("redfish-session-")
    assert result["networks"][0]["connectivity"]["reachable"] is True
    assert result["power"][0]["power_state"] == "On"
    assert result["networks"][0]["bond"]["mode"] == "lacp"
