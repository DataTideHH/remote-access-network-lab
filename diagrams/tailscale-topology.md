# Tailscale topology diagram

This diagram shows the anonymized remote-access topology used in the lab.

No real Tailscale IP addresses, private LAN addresses, SSH fingerprints or account-specific details are included.

```mermaid
flowchart LR
  subgraph Clients["Trusted client devices"]
    TP["Windows ThinkPad X1<br/>mobile client"]
    OP["Windows school desktop<br/>BBQ OptiPlex Tower"]
    IP["iPhone 12 Pro Max<br/>mobile validation"]
  end

  TS["Tailscale Tailnet<br/>private mesh VPN"]
  IM["macOS workstation<br/>iMac remote access target"]

  TP --> TS
  OP --> TS
  IP --> TS
  TS --> IM

  TP -. "tested: SSH over Tailscale" .-> IM
  OP -. "tested: Tailscale reachability" .-> IM
```

## Current baseline

- All intended devices were enrolled in the same Tailnet.
- Device-to-device reachability was confirmed.
- SSH from the Windows ThinkPad to the macOS workstation was tested successfully.
- No public port forwarding was configured.
- No exit node, subnet router, Funnel, Serve or Tailscale SSH feature was enabled.
