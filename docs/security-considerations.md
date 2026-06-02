# Security considerations

## Main principle

Remote access must be useful, but it must not unnecessarily increase the attack surface of the home network or personal workstation.

## What will not be published

This repository must never contain:

- private keys
- real public IP addresses
- real device hostnames
- VPN enrollment links
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

Running a public VPN server directly on a productive workstation is a higher operational responsibility. For a more professional setup, a separate gateway such as a router, Raspberry Pi, Linux VM or VPS may be preferable.

## Documentation rule

All configuration examples in this repository must be anonymized and non-functional by design.
