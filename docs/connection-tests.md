# Connection tests

This document records anonymized results from the initial validation period.

Last validated: **June 2026**.

Real addresses, hostnames, account names, fingerprints and Tailnet identifiers are intentionally omitted.

## Test summary

| Validation period | Source role | Target role | Test | Result | Observed path |
|---|---|---|---|---|---|
| June 2026 | Personal macOS target | Institution-managed Windows desktop | Tailscale ping | Passed | DERP relay observed during the recorded test |
| June 2026 | Institution-managed Windows notebook | Personal macOS target | Native SSH over Tailscale, TCP 22 | Passed | Private Tailnet path; no public port forwarding |
| June 2026 | Enrolled test devices | Tailnet control plane | Device visibility | Passed | Devices visible during the recorded test period |

These tests demonstrate selected reachability paths. They do not prove unrestricted communication between all device pairs, permanent online status or a continuously monitored service level.

## Test 1: selected Tailscale reachability

| Field | Result |
|---|---|
| Source | Personal macOS remote target |
| Target | Institution-managed Windows desktop |
| Method | Tailscale ping |
| Result | Successful |
| Path | DERP relay observed during this test |
| Interpretation | Private reachability existed; a direct peer-to-peer path was not established at that moment |

Anonymized observation:

```text
tailscale ping WINDOWS_LAB_DESKTOP
pong from WINDOWS_LAB_DESKTOP via DERP relay
```

A relay path is a valid connectivity result, but it may differ on another network or date.

## Test 2: SSH over Tailscale

| Field | Result |
|---|---|
| Source | `WINDOWS_MOBILE_CLIENT` |
| Target | `MACOS_REMOTE_TARGET` |
| Method | Native SSH over Tailscale |
| Port | TCP 22 |
| Result | Successful |
| Public port forwarding | Not used |
| macOS Remote Login | Enabled for the private test |
| Tailscale SSH | Not enabled |

Anonymized command pattern:

```text
ssh <authorized-user>@MACOS_REMOTE_TARGET
```

Anonymized result:

```text
Authentication completed.
Remote shell opened on the macOS workstation.
```

The actual user name, authentication method, host key and fingerprint are private and are not recorded here.

## Test 3: Tailnet visibility

| Public device role | Visibility during recorded test |
|---|---|
| Personal macOS target | Visible |
| Institution-managed Windows desktop | Visible |
| Institution-managed Windows notebook | Visible |
| Personal mobile validation device | Visible |

Visibility does not itself authorize every service or direction of traffic. Access control must be evaluated separately.

## Availability notes

The institution-managed desktop may become unavailable due to power management, network policy, reassignment or organizational controls.

The personal macOS workstation may be unavailable when powered off, signed out where a user session is required, sleeping, disconnected or not running the required services.

These conditions are expected for a personal learning lab and are not treated as failures of a guaranteed service.

## Revalidation procedure

A future test record should include:

1. validation month or date
2. source and target role names
3. tested service and port
4. pass/fail result
5. whether a direct or relay path was observed
6. whether public port forwarding remained absent
7. whether the device was still authorized
8. only anonymized output

## Publication rule

Do not publish:

- real Tailscale, LAN or public IP addresses
- real hostnames or Tailnet names
- account names or email addresses
- SSH fingerprints, keys or authentication prompts
- enrollment links or QR codes
- raw admin-console screenshots
- complete internal topology
