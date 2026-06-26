# Network Automation

MetalShift treats network state as a required part of bare metal lifecycle
readiness. A server is not ready just because its management controller answers;
the switch-facing path must also be correct, observable, and testable.

## Validation Scope

**Physical switch ports**

- Expected port identifiers and administrative state.
- Link status and negotiated speed where available.
- Host-to-port mapping consistency.

**LACP-style bonds**

- Bond membership and expected member count.
- Active member health.
- Failure evidence when a member link is down or missing.

**VLANs**

- Access or trunk membership expectations.
- Allowed VLAN lists for lifecycle networks.
- Drift detection between intended and observed state.

**IP pools**

- Address allocation availability.
- Subnet, gateway, and reservation consistency.
- Collision or duplicate-assignment detection.

**Connectivity validation**

- Management-plane reachability.
- Host-network reachability after VLAN and IP assignment.
- Clear pass/fail evidence that can be attached to reports.

## Automation Principles

- Validate intent before action.
- Fail with context: device, port, VLAN, pool, and observed state.
- Keep provider-specific API details behind adapters.
- Prefer idempotent checks and safe preflights for public examples.
- Make network readiness visible in the same report as bare metal readiness.

## Example Readiness Question

Before a lifecycle action proceeds, MetalShift should be able to answer:

> Is this host manageable, connected to the expected switch ports, bonded as
> intended, assigned to the correct VLANs and IP pools, and reachable through
> the required paths?

