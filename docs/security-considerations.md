# Security considerations

## Main principle

Remote access must be useful, but it must not unnecessarily increase the attack surface of the home network or personal workstation.

## Current security posture

The current setup uses Tailscale as a private connectivity layer between trusted devices.

No public router port forwarding was configured.

The macOS workstation is reachable over Tailscale for SSH after Remote Login was enabled.

## Features not enabled

The following features were intentionally not enabled during the initial setup:

- Exit Node
- Subnet Router
- Funnel
- Serve
- Tailscale SSH

This keeps the initial lab small and easier to reason about.

## macOS Remote Login

macOS Remote Login was enabled for SSH testing.

Access was limited to admin users.

SSH is intended to be used only through the private Tailnet, not through public internet exposure.

## What will not be published

This repository must never contain:

- private keys
- real public IP addresses
- real private IP addresses
- real Tailscale IP addresses
- real SSH fingerprints
- device enrollment links
- QR codes
- authentication tokens
- screenshots with private account data
- complete internal network details

## Preferred security posture

- Use VPN-based access instead of exposing SSH directly to the internet
- Use trusted devices only
- Keep the number of reachable services small
- Use least privilege where possible
- Document assumptions and limitations
- Treat the macOS workstation as a productive endpoint, not as a general-purpose public server

## Risk considerations

Running a VPN client is low risk when configured correctly.

Running a public VPN server directly on a productive workstation is a higher operational responsibility. For a more professional WireGuard setup, a separate gateway such as a router, Raspberry Pi, Linux VM or VPS may be preferable.

## Documentation rule

All configuration examples in this repository must be anonymized and non-functional by design.
