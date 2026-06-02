# Connection tests

This document records anonymized connection test results.

Real Tailscale IP addresses, SSH fingerprints, local network addresses and account-specific details are intentionally omitted.

## Test 1: macOS workstation to Windows school desktop

| Field | Result |
|---|---|
| Source | macOS workstation |
| Target | Windows school desktop / BBQ OptiPlex Tower |
| Method | Tailscale ping |
| Result | Successful |
| Path | Relay path observed during initial test |
| Notes | Direct peer-to-peer connectivity was not established during the first test, which is acceptable for the initial working state. |

Anonymized observation:

```text
tailscale ping windows-school-desktop
pong from windows-school-desktop via DERP relay
direct connection not established
```

## Test 2: Windows ThinkPad to macOS workstation via SSH

| Field | Result |
|---|---|
| Source | Windows ThinkPad X1 |
| Target | macOS workstation |
| Method | SSH over Tailscale |
| Result | Successful |
| Public port forwarding | Not used |
| macOS Remote Login | Enabled |
| Access scope | Admin users only |

Anonymized command:

```text
ssh user@example-macos-workstation
```

Anonymized result:

```text
Login successful.
Remote shell opened on the macOS workstation.
```

## Test 3: Device visibility

| Device role | Tailnet visibility |
|---|---|
| macOS workstation | Visible |
| Windows school desktop | Visible during initial test |
| Windows ThinkPad X1 | Visible |
| iPhone 12 Pro Max | Visible |

## Notes

The Windows school desktop may go offline after the user session is locked or when school-network power management takes effect.

This is acceptable for the current lab state because the primary remote access use case is the Windows ThinkPad connecting to the macOS workstation at home.

## Publication rule

Do not publish:

- real Tailscale IP addresses
- SSH fingerprints
- private LAN addresses
- real account names
- authentication prompts
- VPN enrollment links
