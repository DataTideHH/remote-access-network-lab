# Validation checklist

Use this checklist before publishing changes or revalidating the lab.

## Repository safety

Verify that the repository does not contain:

- [ ] private keys, auth keys or authentication tokens
- [ ] device enrollment links or QR codes
- [ ] real public, private or Tailscale IP addresses
- [ ] real hostnames, Tailnet names or account identities
- [ ] real SSH fingerprints or authorized-key material
- [ ] private Tailnet policy exports
- [ ] organization-specific asset or management identifiers
- [ ] screenshots with private account, device or infrastructure data
- [ ] complete internal topology
- [ ] raw command output that has not been reviewed and sanitized

## Documentation consistency

Verify that:

- [ ] README and detailed documents describe the same current state
- [ ] recorded tests include a validation date
- [ ] device visibility is not described as unrestricted service access
- [ ] selected tests are not generalized to every device pair
- [ ] the macOS workstation is not described as having an availability commitment
- [ ] institution-managed devices are described as temporary and authorization-dependent
- [ ] planned controls are not described as already implemented
- [ ] the exact private access policy is not published
- [ ] every example is clearly synthetic or anonymized

## Device authorization and lifecycle

For each enrolled device, verify privately:

- [ ] ownership or organizational permission is still valid
- [ ] the device is still needed for the documented use case
- [ ] the device is approved if approval is required
- [ ] key-expiry behavior is known and appropriate
- [ ] the Tailscale client is current
- [ ] management status has not changed unexpectedly
- [ ] return, reassignment, loss or compromise has not triggered offboarding
- [ ] stale devices have been disabled or removed

## Access-control review

Verify privately:

- [ ] the source role is authorized
- [ ] the destination role is correct
- [ ] only the required service and port are permitted
- [ ] general client-to-client access is not assumed
- [ ] unrelated personal devices are not included by accident
- [ ] mobile validation does not imply SSH permission
- [ ] subnet routes and exit-node routes remain outside the baseline
- [ ] Funnel, Serve and Tailscale SSH remain disabled unless separately reviewed

## Native SSH validation

For the documented path, verify privately:

- [ ] the macOS target is available
- [ ] Remote Login is enabled only as intended
- [ ] the intended account is authorized
- [ ] TCP 22 is permitted through the private path
- [ ] public router port forwarding remains absent
- [ ] authentication material is current
- [ ] stale client authorization has been removed
- [ ] no user name, key or fingerprint is copied into public evidence

## Connection-test record

A public test record should include only:

- [ ] validation date or month
- [ ] public source role
- [ ] public target role
- [ ] tested service and port
- [ ] pass/fail result
- [ ] direct or relay path if relevant
- [ ] confirmation that public port forwarding was absent
- [ ] a statement of limitations

## Local repository validation

Before committing:

```bash
python scripts/validate_public_repository.py
git status --short
git diff --check
git diff
```

Verify that:

- [ ] the validation script passes
- [ ] only intended files changed
- [ ] no generated local configuration was added
- [ ] no secret-like value appears in the diff
- [ ] the commit message describes the actual change

## Offboarding

When a device is returned, reassigned, lost, compromised or no longer required:

- [ ] disable or remove it from the Tailnet
- [ ] revoke relevant authentication material
- [ ] review tags, groups and grants
- [ ] remove dedicated SSH authorization where applicable
- [ ] revalidate the remaining approved path
- [ ] publish only an anonymized outcome

## Review principle

A useful change should make the lab safer, clearer or easier to validate. Do not add public exposure, infrastructure products or broad permissions solely to make the repository appear more advanced.
