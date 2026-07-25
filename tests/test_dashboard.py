import json
from pathlib import Path
from urllib.request import urlopen

import pytest
from playwright.sync_api import Page, expect

from metalshift.dashboard import build_status_payload


def test_status_payload_summarizes_vendor_neutral_environments() -> None:
    payload = build_status_payload()

    assert payload["status"] == "Ready"
    assert payload["summary"] == {"environments": 3, "hosts": 6, "networks": 3}
    assert {environment["name"] for environment in payload["environments"]} == {
        "lab_a",
        "staging",
        "smoke",
    }


def test_dashboard_health_endpoint(dashboard_server: tuple[str, int]) -> None:
    host, port = dashboard_server

    with urlopen(f"http://{host}:{port}/health", timeout=2) as response:
        payload = json.loads(response.read())

    assert response.status == 200
    assert payload == {"status": "ok"}


@pytest.mark.browser
def test_operator_can_review_environment_readiness(
    page: Page,
    dashboard_server: tuple[str, int],
) -> None:
    host, port = dashboard_server

    page.goto(f"http://{host}:{port}")

    expect(page).to_have_title("MetalShift Validation Control")
    expect(page.get_by_role("heading", name="MetalShift Validation Control")).to_be_visible()
    expect(page.locator("#status")).to_have_text("Ready")
    expect(page.locator("#hosts")).to_have_text("6")
    expect(page.get_by_role("table", name="Environment readiness")).to_be_visible()
    Path("artifacts").mkdir(exist_ok=True)
    page.screenshot(path="artifacts/metalshift-dashboard.png", full_page=True)
