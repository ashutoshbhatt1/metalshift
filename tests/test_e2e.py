import pytest

from metalshift.models.environments import all_environment_data
from metalshift.testsets.e2e import E2ETestSet


@pytest.mark.e2e
@pytest.mark.parametrize("environment_data", all_environment_data(), ids=lambda data: data.environment.name)
def test_e2e_runs_for_all_vendor_neutral_environments(
    environment_data, api_client, redfish_client, network_client, test_record
):
    testset = E2ETestSet(test_record, api_client, redfish_client, network_client, environment_data)
    result = testset.run()

    assert result["environment"] in {"lab_a", "staging", "smoke"}
    assert result["summary"]["hosts_configured"] == len(environment_data.hosts)
    assert result["summary"]["networks_configured"] == len(environment_data.networks)
