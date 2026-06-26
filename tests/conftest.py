"""Shared pytest fixtures for MetalShift."""

from pathlib import Path

import pytest

from framework.record import TestType
from framework.report import Report
from metalshift.clients.api_client import APIClient
from metalshift.clients.auth_client import AuthClient
from metalshift.clients.network_client import NetworkClient
from metalshift.clients.redfish_client import RedfishClient
from metalshift.models.environments import all_environment_data, lab_a_data


@pytest.fixture
def all_environment_names():
    return [data.environment.name for data in all_environment_data()]


@pytest.fixture
def lab_environment():
    return lab_a_data()


@pytest.fixture
def report(tmp_path):
    return Report(name="MetalShift Test Report", output_dir=tmp_path)


@pytest.fixture
def test_record(report):
    return report.new_test_record("pytest-record", TestType.TEST)


@pytest.fixture
def artifact_dir(tmp_path) -> Path:
    return tmp_path


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def auth_client():
    return AuthClient()


@pytest.fixture
def redfish_client():
    return RedfishClient()


@pytest.fixture
def network_client():
    return NetworkClient()
