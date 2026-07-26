# Troubleshooting

Troubleshooting should distinguish connectivity, service availability, authorization and device-lifecycle problems. Output must be anonymized before publication.

## Device not visible or reachable

Check privately:

- the device is powered on and connected
- the Tailscale client is running
- the device is authenticated to the expected Tailnet
- the device is approved if approval is required
- the device key has not expired
- the device is still authorized and needed
- the correct private device name is being used
- the access policy permits the intended source, destination and service

Do not publish the real device name, Tailnet name or address while documenting the result.

## Tailscale visibility works but the service does not

Tailnet visibility does not prove that a particular service is reachable.

Check:

- the destination service is running
- the service is listening on the expected interface and port
- the local firewall permits the traffic
- the private Tailnet policy permits the path
- the source device is in the intended role
- the destination device is available

## Native SSH does not connect

For the documented macOS target, check privately:

- Remote Login is enabled
- the intended local account is authorized
- the SSH service is listening on TCP 22
- Tailscale is connected on both endpoints
- the access policy permits TCP 22 from the client role to the target role
- the authentication method is still valid
- no stale host-key or account assumption is being used

macOS checks:

```text
sudo systemsetup -getremotelogin
sudo lsof -iTCP:22 -sTCP:LISTEN -n -P
```

Sanitize command output before publication. Do not publish login names, fingerprints, keys or full SSH configuration.

## Access policy denies a valid use case

Review:

- source role or tag
- destination role or tag
- required protocol and port
- whether the device was approved
- whether the rule is intentionally absent
- whether the requested access expands the documented scope

Do not solve a narrow policy issue by granting broad client-to-client or all-port access without a separate review.

## Tailscale ping uses DERP

A DERP relay path is not automatically a failure. It indicates that a direct peer-to-peer path was not established for that test.

Possible causes include:

- restrictive NAT
- firewall or UDP restrictions
- school or enterprise network policy
- temporary network conditions

Record the observed path with a validation date. Do not describe it as a permanent property of the architecture.

## Institution-managed device appears offline

Possible causes include:

- sleep or power management
- school-network restrictions
- Tailscale service state
- reassignment or endpoint-management changes
- expired authorization or device key
- device return or decommissioning

Before restoring access, confirm that continued enrollment remains permitted and necessary.

## Device should no longer have access

Treat return, loss, compromise, reassignment or loss of authorization as an offboarding event:

1. disable or remove the device from the Tailnet
2. revoke relevant authentication material
3. review groups, tags and grants
4. remove dedicated SSH authorization where applicable
5. revalidate the remaining approved path
6. publish only an anonymized outcome

## VPN connects but no traffic flows

Check:

- device approval and key status
- policy grants
- local firewall
- service-specific permissions
- name resolution
- route assumptions
- whether subnet or exit-node routing was incorrectly assumed

The current baseline does not enable subnet routing or an exit node.

## macOS target is unavailable

Check:

- power and sleep state
- active network connectivity
- required user-session state
- Tailscale client state
- Remote Login state
- local firewall

The iMac is a personal productive endpoint, not an always-available server.

## Documentation rule

Before adding troubleshooting evidence:

- replace real hostnames with public role names
- remove addresses, account names and fingerprints
- avoid raw admin-console screenshots
- state the validation date
- distinguish observed facts from hypotheses
- run `python scripts/validate_public_repository.py`
