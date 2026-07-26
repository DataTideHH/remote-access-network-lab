# Access-control model

## Status

This document defines the intended public-safe access model for the current remote-access lab.

It does not publish the private Tailnet policy and does not claim that every rule below is already deployed exactly as written. Private implementation must be verified separately before use.

## Security objective

The remote-access path should provide only the access required for the documented use case:

```text
approved Windows client -> macOS target -> native SSH on TCP 22
```

The model should not create general lateral access between all enrolled devices.

## Device roles

| Public role | Trust context | Intended access |
|---|---|---|
| `remote-target` | Personal macOS workstation | Receives narrowly scoped remote administration traffic when available |
| `managed-client` | Institution-managed Windows device used temporarily with permission | May initiate only the approved remote-access flow |
| `mobile-validation` | Personal mobile device | Connectivity validation only unless a separate need is documented |
| `unrelated-device` | Other personal or lab endpoint | No access implied by this project |

Real hostnames, user identities, tags and device IDs are private and must not be copied into this repository.

## Intended grants

The public target model permits:

- approved `managed-client` devices to reach `remote-target` on TCP 22
- administrative control-plane actions only by the private Tailnet administrator

The public target model does not require:

- arbitrary ports from the managed client to the target
- access from the target back to the managed client
- managed-client access to unrelated devices
- mobile-client access to SSH
- client-to-client traffic
- subnet routes
- exit-node routes
- public ingress through Funnel or Serve

Rules should be deny-by-omission: traffic is not granted unless the documented use case requires it.

## Policy implementation boundary

Tailscale supports policy-based access control. The current public example uses role tags and a `grants` rule because this expresses the intended source, destination and network capability without publishing real identities.

The example under `examples/tailnet-policy.example.hujson` is deliberately non-functional:

- it uses generic role tags
- it contains no real users or devices
- it is not an export from the private Tailnet
- it must be reviewed in the private environment before any adaptation

## Device approval and key lifecycle

The private Tailnet review should answer:

1. Is device approval enabled or otherwise handled deliberately?
2. Who may approve a new device?
3. Is the device still authorized and required?
4. Is key expiry enabled and appropriate for the role?
5. Is the client software current?
6. Has a returned, lost or reassigned device been removed promptly?

Institution-managed devices should not receive indefinite trust merely because they were enrolled successfully once.

## Institution-managed device boundary

A school-managed device may be used only when:

- installation and remote-access use are permitted by the organization
- the device remains under expected management controls
- the access is needed for the documented learning use case
- no organizational data or credentials are copied into the personal lab

The device must be removed or disabled when it is returned, reassigned, lost, no longer authorized or no longer needed.

## SSH boundary

The tested service is native macOS OpenSSH carried over Tailscale connectivity. Tailscale SSH is not enabled.

Public documentation should record:

- source role
- target role
- TCP port 22
- test result and validation date
- whether public port forwarding was absent

Public documentation must not record:

- login names
- passwords
- public or private keys
- SSH fingerprints
- complete `sshd_config` output
- authorized-key files

A private hardening review should prefer the narrowest practical authorized account and key-based authentication. This is a target recommendation, not an implementation claim.

## Offboarding procedure

When a client is no longer trusted or required:

1. disable or remove the device from the Tailnet
2. revoke any relevant authentication material
3. review grants, groups and tags for stale references
4. remove local SSH authorization if it was dedicated to that client
5. record only an anonymized offboarding result in public documentation
6. revalidate the remaining intended access path

## Review triggers

Review this model before adding:

- another user or device category
- broader port access
- subnet routing
- an exit node
- Tailscale SSH
- Funnel or Serve
- a dedicated gateway
- a WireGuard server
- automation using authentication keys
- access from devices outside the trusted personal or authorized institutional scope
