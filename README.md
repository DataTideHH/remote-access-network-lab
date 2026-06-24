# remote-access-network-lab

Documented VPN and remote access learning lab for Windows, macOS and mobile devices.

## Purpose

This repository documents a small, security-conscious remote access lab.

The goal is to understand and document how trusted devices can securely reach a personal workstation without exposing unnecessary services directly to the public internet.

This project is part of my DataTideHH learning portfolio and supports practical learning in networking, VPN concepts, secure remote access, troubleshooting and technical documentation.

## Lab context

The lab environment includes:

- a macOS workstation used as a personal developer machine and intended always-on remote access target
- a Windows 11 school desktop / BBQ OptiPlex Tower used for lab work, documentation, Git/GitHub workflow, Hyper-V and database-related school tasks
- a Windows 11 ThinkPad used as a mobile school / training device and remote access client
- an iPhone 12 Pro Max used as an optional mobile validation client
- VPN-based remote access using Tailscale
- no public secrets, private keys, real IP addresses or sensitive hostnames in this repository

## Current implementation status

The initial Tailscale-based remote access baseline has been tested successfully.

Current state:

- Tailscale is installed on the macOS workstation, the BBQ OptiPlex Tower, the BBQ ThinkPad X1 and the iPhone 12 Pro Max.
- All initially intended devices are enrolled in the same Tailnet.
- All devices can see and communicate with each other.
- SSH from the Windows ThinkPad to the macOS workstation over Tailscale was tested successfully.
- No public port forwarding was configured.
- No exit node, subnet router, Funnel, Serve or Tailscale SSH feature was enabled.

Real Tailscale IP addresses, SSH fingerprints, local network addresses and account-specific details are intentionally omitted.

## Planned approaches

This lab documents two approaches.

### 1. Managed mesh VPN approach

A managed mesh VPN solution such as Tailscale provides practical remote access with less operational overhead.

This approach is useful for:

- simple device enrollment
- NAT traversal without manual router port forwarding
- controlled access between trusted devices
- day-to-day remote access with low maintenance effort
- avoiding direct exposure of SSH or other services to the public internet

This is the practical approach used for the current working lab baseline.

### 2. Self-managed WireGuard lab

WireGuard is included as a technical learning path.

This approach is useful for understanding:

- peers
- public and private keys
- AllowedIPs
- endpoints
- persistent keepalive
- split tunnel versus full tunnel
- routing and firewall implications

The productive remote access setup uses the simpler managed approach, while the WireGuard part is treated as a technical learning lab.

## Repository structure

```text
remote-access-network-lab/
├── README.md
├── docs/
│   ├── architecture.md
│   ├── connection-tests.md
│   ├── decision-records/
│   │   └── 001-managed-mesh-vpn-baseline.md
│   ├── hardware.md
│   ├── portfolio-context.md
│   ├── security-considerations.md
│   ├── setup-notes.md
│   ├── troubleshooting.md
│   └── validation-checklist.md
├── diagrams/
│   ├── .gitkeep
│   └── tailscale-topology.md
├── examples/
│   ├── tailscale-status-example.txt
│   └── wireguard-peer-example.conf
├── .gitignore
└── LICENSE
```

## Network diagram

The anonymized Tailscale topology is documented here:

- [Tailscale topology diagram](diagrams/tailscale-topology.md)

## Learning goals

- understand VPN-based remote access
- compare managed mesh VPN and self-managed VPN approaches
- document a small network architecture clearly
- practice security-aware configuration documentation
- understand basic routing and access control concepts
- use SSH over a private VPN instead of exposing SSH publicly
- avoid publishing secrets, keys, real public IP addresses or private infrastructure details
- build a small but realistic networking portfolio project

## Hardware used

Hardware and operating system details are documented separately:

- [Hardware and operating systems](docs/hardware.md)

Sensitive identifiers such as device IDs, product IDs, serial numbers, public IP addresses, private IP addresses, real VPN addresses, SSH fingerprints and authentication material are intentionally omitted.

## Security principles

This repository intentionally does not contain:

- private keys
- real public IP addresses
- real private IP addresses
- real Tailscale IP addresses
- real SSH fingerprints
- VPN enrollment links
- QR codes
- authentication tokens
- screenshots containing private account data
- complete internal network details

All example configurations are anonymized and non-functional by design.

## Documentation

The following documents are included:

- [Architecture](docs/architecture.md)
- [Decision record: Managed mesh VPN baseline](docs/decision-records/001-managed-mesh-vpn-baseline.md)
- [Hardware and operating systems](docs/hardware.md)
- [Setup notes](docs/setup-notes.md)
- [Connection tests](docs/connection-tests.md)
- [Security considerations](docs/security-considerations.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Portfolio context](docs/portfolio-context.md)
- [Validation checklist](docs/validation-checklist.md)

## Portfolio and validation

This repository is intentionally scoped as a small, documented learning lab rather than a production infrastructure template.

Additional context and review criteria are documented here:

- [Portfolio context](docs/portfolio-context.md)
- [Validation checklist](docs/validation-checklist.md)

## Notes

This is a learning and documentation project, not a production infrastructure template.

The focus is on clear documentation, careful handling of sensitive information and practical understanding of remote access concepts.
