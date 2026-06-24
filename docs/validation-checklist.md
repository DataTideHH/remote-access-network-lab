# Validation checklist

This checklist is used to keep the lab documentation consistent, safe and reproducible without publishing sensitive infrastructure details.

## Repository safety checks

Before publishing changes, verify that the repository does not contain:

- [ ] private keys
- [ ] authentication tokens
- [ ] VPN enrollment links
- [ ] QR codes
- [ ] real public IP addresses
- [ ] real private IP addresses
- [ ] real Tailscale IP addresses
- [ ] real SSH fingerprints
- [ ] real account names where avoidable
- [ ] screenshots with private account or device data
- [ ] complete internal network details

## Documentation checks

Before committing documentation updates, verify that:

- [ ] the README still describes the current lab state accurately
- [ ] architecture notes match the documented device roles
- [ ] connection tests are anonymized
- [ ] security considerations mention features that were intentionally not enabled
- [ ] example configurations are clearly non-functional
- [ ] planned work is not described as already implemented
- [ ] limitations are stated clearly

## Technical validation checks

For the current Tailscale baseline, validate only with anonymized results:

- [ ] devices are visible in the Tailnet
- [ ] the intended remote access target is reachable over Tailscale
- [ ] SSH access works only through the private VPN path
- [ ] no public router port forwarding is required
- [ ] no unnecessary Tailscale features are enabled
- [ ] mobile validation is optional and documented separately if used

## Git workflow checks

Before committing:

- [ ] run git status
- [ ] review git diff
- [ ] check that no generated secrets or local config files were added
- [ ] use a specific commit message
- [ ] keep the commit small and explainable

Suggested commit message for this documentation update:

Add portfolio context and validation checklist

## Review principle

This project should grow in small, reviewable steps.

A useful change should make the lab easier to understand, safer to publish or easier to validate. Changes should not add complexity just to make the repository look larger.
