# Architecture

## Overview

This lab documents secure remote access between trusted personal devices.

The main design goal is to avoid exposing a personal workstation directly to the public internet while still allowing controlled access from trusted clients.

## Conceptual topology

Trusted client device
        |
        | VPN tunnel
        |
VPN / mesh network
        |
        | private VPN address
        |
macOS workstation

## Device roles

| Role | Device type | Purpose |
|---|---|---|
| Remote client | Windows 11 notebook | Access the lab environment from outside the home network |
| Target system | macOS workstation | Personal developer machine and always-on endpoint |
| Optional client | Mobile device | Basic connectivity and reachability testing |

## Approach A: Managed mesh VPN

A managed mesh VPN can simplify:

- device enrollment
- NAT traversal
- identity-based access
- key distribution
- remote access without router port forwarding

This is the preferred practical approach for daily use.

## Approach B: WireGuard lab

A WireGuard setup is useful for learning:

- peers
- key pairs
- AllowedIPs
- endpoint configuration
- persistent keepalive
- split tunnel versus full tunnel
- routing and firewall implications

This approach is treated as a technical lab and should not expose sensitive production systems without a clear security model.

## Design decision

For productive use, the safer and simpler managed approach may be preferred.

For technical understanding, the WireGuard approach is documented separately as a learning exercise.
