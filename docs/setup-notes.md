# Setup notes

## Status

Initial notes only. No production setup has been documented yet.

## Planned setup phases

### Phase 1: Managed remote access test

Planned tasks:

- install VPN client on macOS workstation
- install VPN client on Windows notebook
- verify device visibility
- test ping or equivalent reachability
- test SSH or screen sharing only if explicitly enabled
- observe CPU, RAM and network impact
- document results

### Phase 2: WireGuard learning lab

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
- target device is reachable by VPN address
- local network services are not exposed publicly
- connection survives sleep / reconnect where applicable
- no sensitive values are committed to Git
