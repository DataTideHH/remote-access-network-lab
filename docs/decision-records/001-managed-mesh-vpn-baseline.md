# Decision record 001: Managed mesh VPN baseline

## Status

Accepted for the current learning lab baseline.

## Context

This lab documents remote access between trusted personal devices.

The practical requirement is to reach a personal macOS workstation securely from trusted clients without exposing SSH or other services directly to the public internet.

The lab also has a learning goal: understanding VPN concepts, remote access design, security boundaries, troubleshooting and technical documentation.

Two approaches are relevant:

- a managed mesh VPN approach using Tailscale
- a self-managed WireGuard approach as a technical learning path

## Decision

The current practical baseline uses Tailscale as the managed mesh VPN layer.

WireGuard remains included as a separate learning path, but not as the productive baseline for this lab.

The current baseline does not enable:

- public router port forwarding
- Exit Node
- Subnet Router
- Funnel
- Serve
- Tailscale SSH

SSH access to the macOS workstation is tested only over the private Tailnet.

## Rationale

Tailscale is appropriate for the current baseline because it reduces operational complexity while still supporting the main learning and access goals.

The managed mesh VPN approach provides:

- simple device enrollment
- NAT traversal without manual router configuration
- private connectivity between trusted devices
- lower maintenance effort for a personal learning lab
- a safer default posture than exposing SSH directly to the public internet
- a realistic remote access setup across macOS, Windows and iOS devices

WireGuard remains valuable for learning because it exposes lower-level VPN concepts such as peers, key pairs, AllowedIPs, endpoints, persistent keepalive, routing and firewall implications.

For this lab, the safer practical choice is to use the managed approach for daily remote access and to keep WireGuard as a separate technical exercise.

## Consequences

Positive consequences:

- the lab has a working and understandable remote access baseline
- no public SSH exposure is required
- the setup is easier to document and validate
- the device roles remain clear
- sensitive infrastructure details can stay anonymized
- the lab stays small enough to reason about

Trade-offs:

- some lower-level VPN mechanics are abstracted away by the managed service
- the setup depends on an external provider account and control plane
- advanced routing scenarios are intentionally not part of the current baseline
- this is not a complete enterprise remote access architecture

## Security notes

The current baseline intentionally keeps the reachable service set small.

The following items must not be published:

- private keys
- authentication tokens
- VPN enrollment links
- real public IP addresses
- real private IP addresses
- real Tailscale IP addresses
- real SSH fingerprints
- complete internal network details

## Review trigger

This decision should be reviewed if the lab later adds:

- a dedicated gateway device
- subnet routing
- exit node functionality
- public service exposure
- WireGuard server operation
- a Raspberry Pi, router, Linux VM or VPS as a VPN endpoint
- broader access for devices beyond the trusted personal lab environment
