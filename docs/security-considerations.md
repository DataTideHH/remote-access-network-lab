# Security considerations

## Main principle

Remote access must solve a specific access need without creating unnecessary exposure, lateral movement or permanent trust.

## Current verified posture

Last validated: **June 2026**.

The recorded baseline used Tailscale as a private connectivity layer between selected trusted or authorized devices.

Verified properties:

- no public router port forwarding was configured
- the macOS workstation was reachable through Tailscale for native SSH after Remote Login was enabled
- SSH from the institution-managed Windows notebook to the macOS target succeeded
- selected Tailscale reachability and Tailnet visibility checks succeeded
- Exit Node, Subnet Router, Funnel, Serve and Tailscale SSH were not enabled

These statements describe the recorded test period. They are not a permanent availability or policy-compliance guarantee.

## Trust categories

Devices are not considered equally trusted merely because they are enrolled in the same Tailnet.

| Category | Security treatment |
|---|---|
| Personal remote target | Productive endpoint; expose only the required private service |
| Institution-managed client | Temporary, authorization-dependent and subject to offboarding |
| Personal mobile validation device | Visibility testing only unless another need is approved |
| Unrelated device | No access implied by this lab |

## Access-control principle

The intended public model is deny-by-omission:

- grant only the required source-to-destination path
- restrict the service to native SSH on TCP 22
- do not grant general client-to-client access
- do not grant access to unrelated personal systems
- do not publish the real Tailnet policy

See [Access-control model](access-control-model.md).

## Device approval and key lifecycle

The private administrative review should cover:

- whether new devices require explicit approval
- who may approve them
- whether key expiry is enabled and appropriate
- whether the client remains current
- whether the device is still needed and authorized
- whether returned, lost, compromised or reassigned devices have been removed

No device should retain indefinite access solely because its initial enrollment succeeded.

## Institution-managed devices

School-managed systems are not permanent personal infrastructure.

Use is conditional on organizational permission. The lab must not:

- bypass endpoint-management controls
- copy organizational credentials or data into the personal environment
- create undeclared persistent access
- retain the device in the Tailnet after it is returned or no longer needed

Offboarding is required when authorization, ownership, assignment or trust changes.

## Native macOS SSH

The tested service is native macOS OpenSSH transported over Tailscale. Tailscale SSH is not enabled.

Public documentation may state:

- the source and target roles
- TCP port 22
- whether the test passed
- the validation date
- that public port forwarding was absent

Public documentation must not include:

- local login names
- passwords
- private or public keys
- SSH fingerprints
- authorized-key files
- complete SSH configuration output

A private hardening review should prefer:

- the narrowest practical authorized account
- key-based authentication where practical
- a clear revocation path
- removal of stale authorization

These are target controls, not claims that every item is already implemented.

## Features intentionally outside the baseline

- public SSH exposure
- Tailscale SSH
- Exit Node
- Subnet Router
- Funnel
- Serve
- public WireGuard server operation
- broader routing to the home network

Adding any of these requires a separate architecture and security review.

## Availability boundary

The macOS workstation is a personal productive endpoint, not an always-available server. Reachability depends on power state, user session, networking, Tailscale state, SSH service state and local permissions.

## Public repository exclusions

This repository must never contain:

- private keys or authentication tokens
- auth keys, enrollment links or QR codes
- real public, private or Tailscale IP addresses
- real hostnames, Tailnet names or account identities
- SSH fingerprints or authorized keys
- private policy exports
- raw admin-console exports
- screenshots with private account or device data
- complete internal topology
- organization-specific asset or management identifiers

## Incident and offboarding response

If a device is lost, compromised, returned, reassigned or no longer authorized:

1. disable or remove it from the Tailnet
2. revoke relevant authentication material
3. review tags, groups and grants
4. remove dedicated SSH authorization where applicable
5. revalidate the remaining approved path
6. record only an anonymized outcome publicly

## Documentation rule

Every public example must be synthetic or anonymized, clearly labelled and independently reviewed before publication. The repository validator is a guardrail, not a substitute for manual review.