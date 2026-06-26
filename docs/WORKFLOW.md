# MetalShift Workflow

MetalShift demonstrates a practical flow for validating bare metal and network
readiness before lifecycle automation is trusted in a larger environment.

## Workflow Stages

1. **Inventory input**
   - Load host, BMC, switch port, VLAN, and IP pool data from a neutral source.
   - Keep sensitive credentials and environment-specific values outside public
     fixtures.

2. **Management access validation**
   - Confirm Redfish-style BMC login behavior.
   - Record authentication and response-shape evidence.

3. **Client boundary checks**
   - Exercise API, BMC, and network-controller boundaries with mocked clients.
   - Keep provider-specific implementation details outside workflow tests.

4. **Network readiness validation**
   - Confirm physical switch port expectations.
   - Validate LACP-style bonds and member links.
   - Check VLAN membership and IP pool allocation.
   - Run connectivity validation before lifecycle actions proceed.

5. **Lifecycle checks**
   - Execute safe preflight and state-transition tests.
   - Keep destructive operations behind explicit configuration gates.

6. **Reporting**
   - Convert test results into readable engineering evidence.
   - Summarize risk, readiness, and next actions for leadership review.

## Pytest Marker Strategy

- Use `smoke` for quick confidence checks.
- Use `network` when switch ports, bonds, VLANs, IP pools, or connectivity are
  part of the validation path.
- Use `lifecycle` for bare metal state and management workflows.
- Use `reporting` for artifact and summary validation.
- Use `e2e` for complete orchestration scenarios.

## Public Showcase Boundaries

The showcase avoids private environment names, vendor-specific assumptions, and
production credentials. Examples should be portable, readable, and safe to share
with recruiters, hiring managers, and engineering interviewers.
