# Setup notes

## Status

The initial managed remote access baseline has been completed.

Tailscale was installed and tested on all initially intended devices:

- macOS workstation
- Windows school desktop / BBQ OptiPlex Tower
- Windows ThinkPad X1
- iPhone 12 Pro Max

All devices were enrolled in the same Tailnet and were able to see and communicate with each other.

## Phase 1: Managed remote access test

Completed tasks:

- installed Tailscale on the macOS workstation
- installed Tailscale on the Windows school desktop
- installed Tailscale on the Windows ThinkPad
- installed Tailscale on the iPhone
- verified Tailnet visibility
- tested reachability between devices
- enabled macOS Remote Login for SSH
- tested SSH from the Windows ThinkPad to the macOS workstation over Tailscale
- kept all real Tailscale IP addresses and SSH fingerprints out of Git

## SSH test

The first practical remote access use case was:

```text
Windows ThinkPad X1
        |
        | SSH over Tailscale
        |
macOS workstation at home
```

The SSH test succeeded.

The first SSH host key prompt was accepted after verifying the intended Tailscale hostname.

No public router port forwarding was used.

## Features intentionally not enabled

The following Tailscale features were intentionally not enabled during the initial setup:

- Exit Node
- Subnet Router
- Funnel
- Serve
- Tailscale SSH

The current setup uses Tailscale only as a private connectivity layer between trusted devices.

## Phase 2: WireGuard learning lab

Planned tasks:

- create WireGuard key pairs
- define peers
- document AllowedIPs
- test split tunnel behavior
- document routing assumptions
- document troubleshooting steps
- keep all secrets out of Git

## Test checklist

- VPN client starts successfully
- target device is reachable by Tailscale name
- local network services are not exposed publicly
- SSH works over Tailscale
- real Tailscale IP addresses are not committed
- SSH fingerprints are not committed
- no sensitive values are committed to Git
