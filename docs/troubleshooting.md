# Troubleshooting

## Device not reachable

Check:

- VPN client is running on both devices
- device is online
- device is logged into the expected Tailnet
- correct Tailscale device name is used
- local firewall allows the intended service
- target service is actually enabled

## SSH does not connect

Check:

- Remote Login is enabled on the macOS target
- SSH server is listening on port 22
- Tailscale connection is active
- correct Tailscale hostname is used
- correct macOS user name is used
- the user is allowed to use Remote Login
- firewall does not block SSH

On macOS, Remote Login can be checked with:

```text
sudo systemsetup -getremotelogin
```

SSH listening state can be checked with:

```text
sudo lsof -iTCP:22 -sTCP:LISTEN -n -P
```

## Tailscale ping works only via DERP relay

This is not automatically a failure.

A DERP relay path means Tailscale could not establish a direct peer-to-peer connection and used a relay instead.

Possible reasons:

- restrictive NAT
- firewall rules
- school or enterprise network restrictions
- UDP restrictions
- temporary network conditions

For the initial lab state, reachability through DERP is acceptable.

## Windows school desktop appears offline

Possible reasons:

- Windows is sleeping
- network adapter power saving is active
- school network disconnected idle clients
- Tailscale service is not active
- user session was locked and background connectivity changed

This is acceptable for the current lab if the primary use case is ThinkPad to macOS workstation.

## VPN connects but no traffic flows

Check:

- Tailnet device status
- route configuration
- local firewall rules
- service-specific permissions
- name resolution
- split tunnel assumptions

## macOS target wakes or sleeps unexpectedly

Check:

- Energy Saver settings
- wake for network access
- external SSD sleep behavior
- Remote Login state
- whether the iMac is expected to stay reachable continuously

## Documentation rule

Any troubleshooting output added to this repository must be anonymized before publishing.
