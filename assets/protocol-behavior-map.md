# Protocol Behavior Map

This document outlines expected behaviors and potential anomalies for common network protocols.  
It serves as a reference for threat detection, forensic analysis, and intrusion prevention systems.

---

## 🧩 Protocols Overview

| Protocol | Normal Behavior | Suspicious Behavior |
|---------|------------------|----------------------|
| HTTP    | GET/POST requests to known domains | Large POST to unknown IP, encoded payloads |
| DNS     | Resolving known domains | High-frequency queries, NXDOMAIN spikes |
| FTP     | Authenticated file transfer | Anonymous login, upload to external server |
| SMTP    | Sending mail via trusted relay | Outbound spam bursts, spoofed headers |
| SSH     | Admin access from internal IP | Brute-force attempts, login from foreign IP |
| ICMP    | Ping for connectivity | Flooding, tunneling payloads |
| TLS     | Encrypted session to known host | Self-signed certs, expired certs, uncommon ports |

---

## 🛡️ Use Cases

- Threat hunting
- Log correlation
- Protocol anomaly detection
- SOC playbook integration

---

## 📖 Notes

- This map is not exhaustive. Protocol behavior may vary by environment.
- Always correlate with endpoint and context data before flagging anomalies.
