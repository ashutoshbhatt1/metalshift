# MetalShift

[![MetalShift CI](https://github.com/ashutoshbhatt1/metalshift/actions/workflows/ci.yml/badge.svg)](https://github.com/ashutoshbhatt1/metalshift/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![PyTest](https://img.shields.io/badge/tests-PyTest-0A9EDC?logo=pytest&logoColor=white)](https://pytest.org/)
[![Playwright](https://img.shields.io/badge/browser-Playwright-2EAD33?logo=playwright&logoColor=white)](https://playwright.dev/python/)

MetalShift is a public showcase for vendor-neutral bare metal and network
lifecycle automation. It demonstrates how a pytest-based framework can validate
server access, network readiness, workflow orchestration, and report generation
without depending on a specific hardware vendor or private lab.

## What It Demonstrates

- Pytest-driven lifecycle workflows for bare metal infrastructure.
- Redfish-style BMC login validation with clean client boundaries.
- API, BMC, and network client boundaries that can later connect to real providers.
- Network automation as a first-class capability: physical switch ports,
  LACP-style bonds, VLANs, IP pools, and connectivity validation.
- Public-ready reporting that turns technical test evidence into concise
  operational summaries.
- Playwright validation of a synthetic operator dashboard and its asynchronous
  environment-readiness data.
- CI quality gates for linting, type checking, multiple Python versions, JUnit
  reports, screenshots, and browser traces.

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[test]"
python -m playwright install chromium
python -m pytest -m "not browser"
python -m pytest -m browser --browser chromium
```

Run the synthetic operator dashboard:

```bash
metalshift-dashboard --port 8080
```

## Repository Map

```text
metalshift/
├── metalshift/              # Package modules for clients, models, and testsets
├── tests/                   # Public showcase tests
├── docs/                    # Architecture, workflow, network, and reporting notes
├── assets/                  # Mermaid architecture diagram source
├── artifacts/               # CI-generated JUnit and Playwright evidence
├── pyproject.toml           # Package metadata and pytest configuration
└── .github/workflows/       # Matrix CI and browser validation
```

## Use Cases

- Validate that a bare metal host exposes expected management access before a
  lifecycle action proceeds.
- Confirm that switch-facing configuration is ready: correct ports, bonded
  links, VLAN membership, address pool allocation, and end-to-end reachability.
- Exercise lifecycle workflows while keeping test output readable for engineers
  and leaders.
- Produce recruiter-friendly artifacts that explain the automation approach,
  tradeoffs, and roadmap without exposing proprietary environments.

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Workflow](docs/WORKFLOW.md)
- [Network Automation](docs/NETWORK_AUTOMATION.md)
- [Telemetry Roadmap](docs/TELEMETRY_ROADMAP.md)
- [Mermaid Architecture Asset](assets/architecture.md)

## Testing Themes

MetalShift organizes validation around pytest markers:

- `smoke`: quick framework and fixture checks.
- `lifecycle`: bare metal lifecycle workflows.
- `network`: switch ports, bonds, VLANs, IP pools, and connectivity.
- `reporting`: report artifact validation.
- `e2e`: complete orchestration paths.
- `browser`: Playwright validation of operator-facing readiness evidence.

## CI Evidence

Every pull request runs:

1. Ruff linting and MyPy type analysis.
2. PyTest unit, network, lifecycle, reporting, and end-to-end tests on Python
   3.10 and 3.12.
3. A Chromium Playwright workflow that verifies dashboard rendering and API data.
4. Uploads of JUnit XML, the dashboard screenshot, and failure traces.

This provides reviewable evidence instead of relying only on console logs.

## Positioning

This project is intentionally vendor-neutral. The patterns apply to any
environment that exposes management-plane APIs, Redfish-style BMC access,
switch automation interfaces, and observable lifecycle outcomes. All endpoints,
credentials, hostnames, and network ranges are synthetic and safe for public
demonstration.
