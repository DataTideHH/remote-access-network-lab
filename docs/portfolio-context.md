# Portfolio context

## Why this project exists

This repository documents a small remote access and VPN learning lab.

The goal is not to present a production-ready enterprise VPN architecture. Instead, the project shows how a security-conscious remote access setup can be planned, tested and documented in a realistic personal learning environment.

The current baseline uses Tailscale as a managed mesh VPN between trusted devices. WireGuard is included as a separate learning path for understanding lower-level VPN concepts.

## What this project demonstrates

This project demonstrates practical understanding of:

- VPN-based remote access
- secure access to a workstation without public port forwarding
- device roles in a small network environment
- SSH over a private VPN
- documentation of technical assumptions and limitations
- anonymization of sensitive infrastructure details
- basic operational validation through connection tests

## Relation to my learning path

This lab supports my Fachinformatiker Daten- und Prozessanalyse learning path by connecting networking fundamentals with documentation, troubleshooting and structured technical reasoning.

It complements data and BI-focused projects by showing the infrastructure side of practical IT work:

- how systems are reached securely
- how access paths are documented
- how network assumptions are made explicit
- how technical risks are limited and communicated
- how lab results are recorded without exposing private details

## Scope boundaries

This repository intentionally does not claim to be:

- a production VPN template
- a complete zero trust architecture
- a full firewall or routing design
- an enterprise remote access implementation
- a replacement for professional security review

The current scope is a small, realistic learning lab with clear documentation and conservative security assumptions.

## Current maturity level

Current maturity level: documented working lab baseline.

The Tailscale-based setup has been validated for device visibility and SSH access between trusted devices. Further work should stay incremental and should avoid adding unnecessary complexity before the current baseline is fully documented and reviewed.

## Portfolio value

The value of this project is not the amount of code.

The value is the ability to explain:

- what was built
- why a managed VPN approach was chosen
- what was deliberately not enabled
- how the setup was validated
- which sensitive details must not be published
- what would be required before treating a similar setup as production infrastructure
