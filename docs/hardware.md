# Hardware and operating-system roles

This document records only the hardware characteristics needed to explain the lab architecture. Real hostnames, asset identifiers, serial numbers, product IDs, VPN addresses, account names and organization-specific management details are intentionally excluded.

## Personal macOS workstation

| Category | Public-safe value |
|---|---|
| Role | Personal developer workstation and primary remote-access target when available |
| Device class | Apple iMac Retina 4K, 21.5-inch, Late 2015 |
| Model identifier | `iMac16,2` |
| CPU architecture | Intel x86_64 |
| Operating system | macOS Sonoma via OpenCore Legacy Patcher |
| Usage context | Development, portfolio work and personal lab activity |
| Availability boundary | Reachable only when powered on, signed in where required, connected and running the required services |
| Security boundary | Productive endpoint; not a general-purpose public server |

The model and architecture are relevant to reproducibility. The real hostname, addresses, account name, SSH fingerprints and device serial number are not.

## Institution-managed Windows desktop

| Category | Public-safe value |
|---|---|
| Public role name | `WINDOWS_LAB_DESKTOP` |
| Role | School-context Windows lab workstation |
| Device class | x86_64 desktop PC |
| Processor class | Modern Intel Core desktop processor |
| Memory class | 32 GB RAM |
| Operating system | Windows 11 Enterprise |
| Usage context | Selected connectivity tests, Git/GitHub work, documentation, virtualization and database-related school tasks |
| Trust boundary | Institution-managed, temporary and authorization-dependent |

The repository deliberately omits the real device name, asset identifiers, exact OS build, installation date, firmware versions and management-policy details because they are not required to understand the remote-access architecture.

## Institution-managed Windows notebook

| Category | Public-safe value |
|---|---|
| Public role name | `WINDOWS_MOBILE_CLIENT` |
| Role | Mobile school-context client used for the recorded SSH test |
| Device class | Lenovo ThinkPad X1 Carbon Gen 9 |
| Processor class | 11th-generation Intel Core i7, x86_64 |
| Memory class | 16 GB RAM |
| Operating system | Windows 11 Enterprise |
| Usage context | Mobile remote-access client, Git/GitHub verification, documentation and networking practice |
| Trust boundary | Institution-managed, temporary and authorization-dependent |

The repository does not publish the real hostname, model serial, system SKU, BIOS version, exact build number or detailed endpoint-management state.

## Personal mobile validation device

| Category | Public-safe value |
|---|---|
| Public role name | `MOBILE_VALIDATION_CLIENT` |
| Device class | Personal iPhone |
| Operating-system family | iOS |
| Usage context | Optional Tailnet visibility and connectivity validation |
| Trust boundary | Personal device; no SSH permission implied by this role |

The exact VPN address, account identity and device-management identifiers are excluded.

## Why mixed platforms matter

The lab intentionally spans:

- macOS as the remote target
- Windows as the tested remote client and school-context workstation
- iOS as an optional mobile validation platform

This supports cross-platform troubleshooting without turning hardware inventory into an unnecessary disclosure of device-management data.

## Institution-managed device conditions

An institution-managed device may participate only while:

- installation and use are permitted
- the device is still needed for the documented lab purpose
- organizational and personal data remain separated
- the device remains under expected management controls
- the Tailnet enrollment is reviewed and removed during offboarding

Return, reassignment, loss, compromise or withdrawal of authorization is an immediate review trigger.

## Information excluded from the public repository

- real hostnames
- asset tags and device IDs
- serial numbers and product IDs
- exact VPN and LAN addresses
- account identities
- authentication material
- SSH keys and fingerprints
- private Tailnet tags and policy exports
- exact Windows installation dates and volatile build metadata
- detailed organization-specific security-policy configuration
