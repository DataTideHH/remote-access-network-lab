# Portfolio context

## Why this project exists

This repository documents a small remote-access and VPN learning lab with an emphasis on security boundaries, device lifecycle and public-safe technical evidence.

The goal is not to present a production-ready enterprise VPN architecture. The project shows how a practical access path can be selected, tested, limited and documented without publishing private infrastructure details.

## What is implemented

The recorded baseline uses Tailscale as a managed mesh VPN between selected trusted or authorized devices.

Validated in June 2026:

- selected device visibility in the Tailnet
- selected Tailscale reachability
- native SSH from an institution-managed Windows notebook to a personal macOS workstation
- no public router port forwarding
- no Exit Node, Subnet Router, Funnel, Serve or Tailscale SSH

The repository does not claim unrestricted communication between all devices, continuous availability or a published production policy.

## What this project demonstrates

- remote access without public SSH exposure
- difference between connectivity and authorization
- explicit device roles and trust boundaries
- native SSH over a private mesh VPN
- access-control modelling
- temporary trust for institution-managed devices
- key-expiry, approval and offboarding considerations
- dated and anonymized connection evidence
- conservative handling of infrastructure details
- decision records and troubleshooting logic

## Relation to the Data and Process Analysis path

The project complements the main Data/BI portfolio by demonstrating supporting IT foundations:

- how operational systems are reached securely
- how technical access paths are modelled
- how assumptions and controls are documented
- how device lifecycle becomes a repeatable process
- how validation evidence is separated from sensitive raw data
- how risks and limitations are communicated clearly

It supports the broader profile without claiming a separate specialization in network engineering or cybersecurity.

## Scope boundaries

This repository is not:

- a production VPN template
- a complete zero-trust architecture
- a firewall or routing design
- a public WireGuard service
- an enterprise identity architecture
- a continuously monitored remote-access service
- a substitute for organizational authorization or professional security review

## Current maturity

Current maturity: **documented working baseline with explicit public-safety, access-control and offboarding boundaries**.

The technical baseline is intentionally small. Further work should be triggered by a real need or a verified architecture change, not by a desire to add more tools.

## Portfolio value

The value is the ability to explain:

- which access problem was solved
- why a managed mesh VPN was chosen
- what was tested and when
- what the tests do and do not prove
- which features were deliberately excluded
- how access should be limited
- how institution-managed clients are offboarded
- which information must remain private
- what would require a new security review

## Appropriate next milestones

A future milestone would be justified by one of these events:

- a newly authorized client role
- a privately verified least-privilege policy change
- a new dated connection test
- removal or return of an institution-managed device
- a dedicated gateway or lab host
- evaluation of subnet routing or an exit node

Until then, the current baseline should remain stable and easy to review.
