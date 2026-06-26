# Telemetry Roadmap

MetalShift's current public showcase centers on lifecycle, network readiness,
client boundaries, and reporting patterns. The next evolution is telemetry that
turns point-in-time validation into trend-aware operational insight.

## Planned Telemetry Areas

- Redfish sensor collection for temperature, power, fan, and voltage readings.
- Event log ingestion for BMC and hardware lifecycle signals.
- BMC hardware health summaries for processors, memory, storage, power supplies,
  and firmware inventory.
- NIC and link telemetry for carrier state, speed, errors, drops, and member
  health in bonded configurations.
- Switch-facing link history for physical ports, VLAN drift, and connectivity
  changes.
- Lifecycle trend reports that show readiness, failure categories, remediation
  time, and recurring infrastructure risk.

## Reporting Direction

Telemetry should feed the same executive-ready reporting layer used by tests.
The goal is to show not only whether a workflow passed today, but whether the
environment is becoming more stable, more predictable, and easier to operate.

## Public Showcase Constraints

Telemetry examples should use neutral schemas, synthetic data, or safe mock
fixtures. They should demonstrate engineering judgment without exposing private
infrastructure, credentials, or vendor-specific dependencies.
