# Troubleshooting

## Common issues

### Device not reachable

Check:

- VPN client is running on both devices
- device is online
- correct VPN IP address is used
- local firewall allows the intended service
- target service is actually enabled

### SSH does not connect

Check:

- SSH server is enabled on the target machine
- VPN connection is active
- correct VPN address is used
- correct user name is used
- firewall does not block SSH

### VPN connects but no traffic flows

Check:

- route configuration
- AllowedIPs configuration
- split tunnel settings
- firewall rules
- DNS assumptions

### macOS target wakes or sleeps unexpectedly

Check:

- Energy Saver / Battery settings
- wake for network access
- screen sharing / remote login settings
- external SSD sleep behavior if relevant

## Documentation rule

Any troubleshooting output added to this repository must be anonymized before publishing.
