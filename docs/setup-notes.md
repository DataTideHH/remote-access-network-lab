# Setup notes

## Status

The initial managed remote-access baseline was completed and last validated in **June 2026**.

The recorded test period included:

- personal macOS workstation
- institution-managed Windows desktop
- institution-managed Windows notebook
- personal mobile validation device

The devices were enrolled in the same Tailnet during the test period. Tailnet visibility and selected reachability paths were verified. This does not claim unrestricted communication between every device pair or permanent enrollment.

## Preconditions

Before adding a device:

1. confirm ownership or organizational permission
2. define the device role and required destination
3. decide whether explicit device approval is required
4. confirm the expected key-expiry behavior
5. ensure no real device identifier will be published
6. define the offboarding trigger

Institution-managed devices must not be enrolled merely because installation is technically possible.

## Recorded baseline steps

The initial practical workflow was:

1. install Tailscale on the authorized devices
2. authenticate them to the intended private Tailnet
3. verify device visibility
4. verify selected Tailscale reachability
5. enable native macOS Remote Login for the approved access scope
6. test SSH from the Windows mobile client to the macOS target
7. confirm that no public router port forwarding was used
8. record only anonymized results

## Recorded SSH path

```text
WINDOWS_MOBILE_CLIENT
        |
        | native SSH / TCP 22
        | transported over Tailscale
        v
MACOS_REMOTE_TARGET
```

The test succeeded during the recorded validation period.

The public repository does not disclose:

- the real source or target hostname
- the local user name
- the Tailnet name
- addresses
- keys
- fingerprints
- the exact private authentication configuration

## Features outside the baseline

The initial setup did not enable:

- Exit Node
- Subnet Router
- Funnel
- Serve
- Tailscale SSH
- public WireGuard server operation
- public router port forwarding

## Access-control follow-up

The public repository now documents a least-privilege target model. The exact private Tailnet policy is not published and must be reviewed separately.

The intended path permits only the required managed-client-to-macOS-target service. General client-to-client or unrelated-device access is not required.

See [Access-control model](access-control-model.md).

## Device lifecycle

For each enrolled device, review periodically:

- continued authorization
- continued business or learning need
- client version
- key-expiry state
- device approval state
- current management status
- offboarding readiness

Remove or disable a device when it is returned, reassigned, lost, compromised, no longer authorized or no longer required.

## WireGuard learning phase

WireGuard remains a separate learning exercise. Any future implementation should:

- use a dedicated lab boundary rather than the productive workstation where practical
- keep all private keys outside Git
- document peers and `AllowedIPs`
- distinguish split-tunnel and full-tunnel behavior
- document routing and firewall assumptions
- avoid public service exposure without a separate risk review

## Publication checklist

Before publishing setup changes:

- replace real names with role names
- remove exact addresses and fingerprints
- remove organization-specific device identifiers
- verify that planned work is not described as implemented
- run `python scripts/validate_public_repository.py`
- review the final diff manually
