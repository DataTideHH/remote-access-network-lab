# Hardware and operating systems

This document lists the hardware and operating systems used or planned for this remote access network lab.

Sensitive identifiers such as Windows device IDs, product IDs, serial numbers, personal account names, public IP addresses, private IP addresses, VPN addresses and real hostnames are intentionally omitted or anonymized.

## macOS workstation: personal iMac

| Category | Value |
|---|---|
| Role | Personal macOS workstation / intended always-on remote access target |
| Device class | Apple iMac Retina 4K, 21.5-inch, Late 2015 |
| Model identifier | iMac16,2 |
| CPU architecture | Intel x86_64 |
| Operating system | macOS Sonoma via OpenCore Legacy Patcher |
| Usage context | Learning, development, GitHub portfolio work and personal lab environment |
| Notes | Productive developer workstation. Should not be treated as a general-purpose public server. |

## Windows lab machine: BBQ school desktop

| Category | Value |
|---|---|
| Role | Windows lab machine / school desktop |
| Device name | BBQ-BM6HJ64 |
| Device class | Desktop PC |
| CPU | Intel Core i5-14500 |
| Base clock | 2.60 GHz |
| Installed RAM | 32.0 GB |
| Usable RAM | 31.7 GB |
| System type | 64-bit operating system, x64-based processor |
| Pen and touch | No pen or touch input available |
| Operating system | Windows 11 Enterprise |
| Version | 25H2 |
| Installed on | 2026-04-07 |
| OS build | 26200.8390 |
| Windows Feature Experience Pack | 1000.26100.297.0 |
| Usage context | Windows-based testing, Git/GitHub workflow, documentation work, Hyper-V and school-context lab tasks |

## Windows mobile lab machine: BBQ ThinkPad X1 Carbon Gen 9

| Category | Value |
|---|---|
| Role | Windows mobile lab machine / BBQ school notebook |
| Device name | BBQEDU-PF3NRBA0 |
| Manufacturer | Lenovo |
| Model | ThinkPad X1 Carbon Gen 9 |
| System model | 20XXS24W00 |
| System SKU | LENOVO_MT_20XX_BU_Think_FM_ThinkPad X1 Carbon Gen 9 |
| Device class | Notebook |
| Platform role | Mobile |
| CPU | 11th Gen Intel Core i7-1185G7 |
| CPU base clock | 3.00 GHz |
| CPU details | 4 cores, 8 logical processors |
| Installed RAM | 16.0 GB |
| Total physical memory | 15.7 GB |
| Page file | 8.00 GB, C:\pagefile.sys |
| System type | x64-based PC |
| Operating system | Windows 11 Enterprise |
| OS version | 10.0.26200 Build 26200 |
| BIOS mode | UEFI |
| BIOS version/date | Lenovo N32ETA1W (1.77), 2026-02-18 |
| SMBIOS version | 3.2 |
| Embedded controller version | 1.37 |
| Secure Boot state | Off |
| Kernel DMA Protection | On |
| Virtualization-based security | Running |
| Running VBS services | Credential Guard, Hypervisor-enforced Code Integrity, Secure Launch, SMM Firmware Measurement, Kernel-mode Hardware-enforced Stack Protection |
| App Control for Business policy | Enforced |
| App Control for Business user-mode policy | Off |
| SMM isolation level | Firmware Protection Version 2 |
| Hypervisor status | Hypervisor detected |
| Usage context | Mobile Windows test client, school-context device, remote access client, Git/GitHub verification, documentation and networking practice |

## Relevance for this lab

The lab intentionally includes different device types and operating systems:

- macOS as the intended always-on target system
- Windows desktop as a school/lab workstation
- Windows notebook as a mobile client system
- optional mobile device testing later

This allows the project to document remote access and VPN behavior across realistic mixed environments.

## Security and privacy notes

The following values are intentionally not included in this public repository:

- Windows device IDs
- Windows product IDs
- serial numbers
- personal account names
- public IP addresses
- private LAN IP addresses
- VPN-assigned real IP addresses
- private hostnames
- authentication material
- SSH keys
- VPN keys
- tokens
- screenshots containing private account or infrastructure details

## Operational notes

The macOS workstation is the intended always-on endpoint, but it should not be exposed directly to the public internet.

For practical daily use, a managed mesh VPN approach may be preferred.

For technical learning, a separate WireGuard lab can be documented to understand peers, key pairs, AllowedIPs, routing, split tunneling and firewall implications.
