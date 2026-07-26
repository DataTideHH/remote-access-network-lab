# Remote Access Network Lab

Documented, public-safe remote-access learning lab for macOS, Windows and mobile clients.

## Purpose

This repository documents how trusted devices can reach a personal workstation through a private mesh VPN without exposing SSH or other services directly to the public internet.

The project supports practical learning in:

- VPN and remote-access concepts
- device roles and trust boundaries
- SSH over a private network path
- access-control design
- device lifecycle and offboarding
- troubleshooting and technical documentation
- safe publication of infrastructure work

It is a small learning lab, not a production VPN template or an enterprise zero-trust implementation.

## Current verified baseline

Last validated: **June 2026**.

The implemented baseline uses Tailscale as a managed mesh VPN:

- a personal macOS workstation is the primary remote-access target when powered on, signed in and available
- an institution-managed Windows notebook was used as the tested SSH client
- an institution-managed Windows desktop and an iPhone were enrolled for selected reachability and visibility checks
- enrolled devices were visible in the Tailnet during the recorded test period
- selected device-to-device reachability was verified
- native macOS SSH from the Windows notebook to the macOS workstation over Tailscale was tested successfully
- no public router port forwarding was configured
- Exit Node, Subnet Router, Funnel, Serve and Tailscale SSH were not enabled

The recorded tests do not claim permanent availability, unrestricted communication between every device pair or a continuously monitored service.

## Access-control status

The repository documents a least-privilege target model, but it does not publish or claim the exact private Tailnet policy currently in use.

The intended access path is deliberately narrow:

```text
institution-managed Windows client
                |
                | TCP 22 over Tailscale
                v
personal macOS remote-access target
```

The target model does not require:

- general client-to-client access
- access to unrelated personal devices
- subnet routing
- exit-node routing
- public service exposure

See [Access-control model](docs/access-control-model.md) and the non-functional [example policy](examples/tailnet-policy.example.hujson).

## Device trust and lifecycle

Institution-managed school devices are temporary clients, not permanently trusted personal infrastructure. Their use is conditional on organizational permission and continued need.

They should be reviewed and removed from the Tailnet when:

- the device is returned or reassigned
- remote access is no longer required
- authorization changes
- the device is lost, compromised or no longer managed as expected

The documented review includes device approval, key expiry, client updates and offboarding. No real device IDs, hostnames, Tailnet names, account names or authentication material are published.

## SSH model

The tested path uses the native macOS OpenSSH service over Tailscale connectivity. Tailscale SSH is not enabled.

Public documentation records only:

- the source and target roles
- the service and transport path
- the result of the test
- the access boundary

It does not publish usernames, public keys, fingerprints, passwords or the exact private authentication configuration. A future hardening change should prefer a narrowly authorized account and key-based authentication where practical, but this repository does not claim that such a change has already been implemented.

## Managed mesh VPN and WireGuard

### Current practical baseline

Tailscale is used because it provides private device-to-device connectivity and NAT traversal without public router port forwarding or the operational burden of running a public VPN server on the productive workstation.

### Separate learning path

WireGuard remains a conceptual learning path for:

- peers and key pairs
- `AllowedIPs`
- endpoint configuration
- persistent keepalive
- split tunnel versus full tunnel
- routing and firewall implications

The example configuration is intentionally non-functional. No productive WireGuard server is claimed.

## Public-safety boundary

This repository must not contain:

- private keys or authentication tokens
- device enrollment links or QR codes
- real public, private or Tailscale IP addresses
- real hostnames or device-management identifiers
- account names or email addresses used for access control
- SSH fingerprints or authorized-key material
- private Tailnet policy exports
- screenshots containing account, device or infrastructure details
- complete internal network topology

The repository includes a small Python validation script and GitHub Actions workflow that check for selected high-risk patterns and required public-safety artifacts.

Run locally:

```bash
python scripts/validate_public_repository.py
```

## Repository structure

```text
remote-access-network-lab/
├── .github/workflows/ci.yml
├── README.md
├── docs/
│   ├── access-control-model.md
│   ├── architecture.md
│   ├── connection-tests.md
│   ├── decision-records/
│   │   └── 001-managed-mesh-vpn-baseline.md
│   ├── hardware.md
│   ├── portfolio-context.md
│   ├── security-considerations.md
│   ├── setup-notes.md
│   ├── troubleshooting.md
│   └── validation-checklist.md
├── diagrams/
│   └── tailscale-topology.md
├── examples/
│   ├── tailnet-policy.example.hujson
│   ├── tailscale-status-example.txt
│   └── wireguard-peer-example.conf
├── scripts/
│   └── validate_public_repository.py
├── .gitignore
└── LICENSE
```

## Documentation

- [Architecture](docs/architecture.md)
- [Access-control model](docs/access-control-model.md)
- [Decision record: managed mesh VPN baseline](docs/decision-records/001-managed-mesh-vpn-baseline.md)
- [Hardware and operating-system roles](docs/hardware.md)
- [Setup notes](docs/setup-notes.md)
- [Connection tests](docs/connection-tests.md)
- [Security considerations](docs/security-considerations.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Portfolio context](docs/portfolio-context.md)
- [Validation checklist](docs/validation-checklist.md)
- [Anonymized topology](diagrams/tailscale-topology.md)

## Current maturity and next review

Current maturity: **documented working baseline with explicit public-safety and access-control boundaries**.

The next meaningful change should be based on a real review trigger, such as:

- a new authorized client role
- a verified private least-privilege policy change
- a dedicated gateway or lab host
- subnet routing or exit-node evaluation
- a new dated connection test
- retirement or return of an institution-managed device

Complexity should not be added solely to make the repository look larger.