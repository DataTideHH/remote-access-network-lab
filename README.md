# remote-access-network-lab

Documented VPN and remote access learning lab for Windows, macOS and mobile devices.

## Purpose

This repository documents a small, security-conscious remote access lab.

The goal is to understand and document how trusted devices can securely reach a personal workstation without exposing unnecessary services directly to the public internet.

This project is part of my DataTideHH learning portfolio and supports practical learning in networking, VPN concepts, secure remote access, troubleshooting and technical documentation.

## Lab context

The planned lab environment includes:

- a macOS workstation used as a personal developer machine
- a Windows 11 notebook used in a school / training context
- optional mobile device access for basic connectivity checks
- VPN-based remote access
- no public secrets, private keys, real IP addresses or sensitive hostnames in this repository

## Planned approaches

This lab will compare two approaches.

### 1. Managed mesh VPN approach

A managed mesh VPN solution such as Tailscale can provide practical remote access with less operational overhead.

This approach is useful for:

- simple device enrollment
- NAT traversal without manual router port forwarding
- controlled access between trusted devices
- day-to-day remote access with low maintenance effort

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

The productive setup may use the simpler managed approach, while the WireGuard part is treated as a technical learning lab.

## Repository structure

```text
remote-access-network-lab/
├── README.md
├── docs/
│   ├── architecture.md
│   ├── security-considerations.md
│   ├── setup-notes.md
│   └── troubleshooting.md
├── diagrams/
│   └── .gitkeep
├── examples/
│   ├── tailscale-status-example.txt
│   └── wireguard-peer-example.conf
├── .gitignore
└── LICENSE
```

## Learning goals

- understand VPN-based remote access
- compare managed mesh VPN and self-managed VPN approaches
- document a small network architecture clearly
- practice security-aware configuration documentation
- understand basic routing and access control concepts
- avoid publishing secrets, keys, real public IP addresses or private infrastructure details
- build a small but realistic networking portfolio project

## Security principles

This repository intentionally does not contain:

- private keys
- real public IP addresses
- real hostnames
- VPN enrollment links
- QR codes
- authentication tokens
- screenshots containing personal account data
- complete internal network details

All example configurations are anonymized and non-functional by design.

## Current status

Initial repository scaffold.

No production VPN configuration is included yet.

## Planned documentation

The following topics will be documented step by step:

- remote access use case
- device roles
- managed mesh VPN setup notes
- WireGuard lab notes
- connection tests
- troubleshooting notes
- security considerations
- lessons learned

## Notes

This is a learning and documentation project, not a production infrastructure template.

The focus is on clear documentation, careful handling of sensitive information and practical understanding of remote access concepts.
