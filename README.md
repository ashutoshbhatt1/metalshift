# MetalShift

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

## Quick Start

```bash
cd metalshift
python -m pytest
```

## Repository Map

```text
metalshift/
├── metalshift/              # Package modules for clients, models, and testsets
├── tests/                   # Public showcase tests
├── docs/                    # Architecture, workflow, network, and reporting notes
├── assets/                  # Mermaid architecture diagram source
├── pyproject.toml           # Package metadata and pytest configuration
└── pytest.ini               # Local pytest defaults and markers
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

## Positioning

This project is intentionally vendor-neutral. The patterns apply to any
environment that exposes management-plane APIs, Redfish-style BMC access,
switch automation interfaces, and observable lifecycle outcomes.
