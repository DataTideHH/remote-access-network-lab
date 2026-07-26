# Decision record 001: Managed mesh VPN baseline

## Status

Accepted for the current learning lab baseline.

Last reviewed: **July 2026**.

## Context

The practical requirement is to reach a personal macOS workstation from an authorized client without exposing SSH or other services directly to the public internet.

The lab also supports learning in VPN concepts, remote-access design, access control, device lifecycle, troubleshooting and public-safe technical documentation.

Two approaches are relevant:

- managed mesh VPN using Tailscale for the practical baseline
- self-managed WireGuard as a separate technical learning path

## Decision

Use Tailscale as the private connectivity layer for the current practical baseline.

Use native macOS OpenSSH over the Tailnet for the recorded remote shell test. Do not enable Tailscale SSH as part of this baseline.

Do not enable:

- public router port forwarding
- Exit Node
- Subnet Router
- Funnel
- Serve
- public WireGuard server operation

Treat institution-managed Windows devices as temporary, authorization-dependent clients rather than permanent personal infrastructure.

Document a least-privilege target model in which the approved client role requires only TCP 22 access to the macOS target. Do not publish the exact private Tailnet policy.

## Rationale

The managed mesh approach:

- avoids public SSH exposure
- provides NAT traversal without manual router configuration
- supports macOS, Windows and iOS
- reduces the operational burden on the productive workstation
- supports policy-based restrictions
- is easier to validate and revoke than an improvised public VPN service

WireGuard remains valuable for learning peers, keys, `AllowedIPs`, endpoints, routing and firewall behavior, but that learning objective does not justify operating a public VPN server on the personal workstation.

## Consequences

### Positive

- no public SSH port is required
- the remote-access path is small and explainable
- connectivity and authorization can be considered separately
- device roles and trust boundaries are explicit
- temporary clients can be offboarded
- public examples can remain synthetic

### Trade-offs

- the solution depends on an external provider account and control plane
- lower-level WireGuard mechanics are abstracted
- private policy state must be reviewed outside the public repository
- device approval, key expiry and offboarding require ongoing administration
- the personal workstation has no availability commitment

## Access-control consequence

Enrollment alone must not be interpreted as unrestricted authorization.

The target model grants only the required client-to-target service and does not require:

- general client-to-client access
- access to unrelated personal devices
- subnet or exit-node routing
- mobile SSH access
- all-port connectivity

See [Access-control model](../access-control-model.md).

## Institution-managed device consequence

Use of school-managed endpoints is conditional on organizational permission and continued need.

Return, reassignment, loss, compromise or withdrawal of authorization requires prompt removal or disabling of the device and review of related access.

## SSH consequence

The repository may document the tested role-to-role path and TCP port, but it must not publish:

- real login names
- authentication secrets
- public or private keys
- SSH fingerprints
- complete SSH configuration

A future private hardening review should prefer the narrowest practical account scope and key-based authentication where practical. This is a recommendation, not a current implementation claim.

## Public-safety consequence

Do not publish:

- private keys, auth keys or tokens
- enrollment links or QR codes
- real public, private or Tailscale addresses
- real hostnames, account names or Tailnet names
- device-management identifiers
- private policy exports
- raw admin-console screenshots
- complete internal topology

## Review triggers

Review this decision before adding:

- another user or device trust category
- broader port access
- a dedicated gateway
- subnet routing
- exit-node functionality
- Tailscale SSH
- Funnel or Serve
- public service exposure
- WireGuard server operation
- automation using authentication keys
- devices outside the trusted personal or explicitly authorized institutional scope
