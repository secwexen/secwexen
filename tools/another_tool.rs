## another_tool.rs

### Overview

`another_tool.rs` is a Rust module that performs entropy drift analysis across CPU cores and memory regions. It is optimized for environments where real-time detection of covert modulation is required, such as air-gapped systems or forensic platforms.

---

### Capabilities

- Multithreaded entropy sampling
- Hardware telemetry ingestion via `sysfs` and `libc`
- Anomaly scoring based on entropy deviation
- Timestamped alert generation

---

### Execution

```bash
cargo run --release -- --interval 50 --threshold 0.72
```

---

### Parameters

- `--interval`: Sampling interval in milliseconds
- `--threshold`: Entropy deviation threshold (0.0–1.0)

### Output

Alerts are printed to stdout and optionally logged to `logs/entropy_alerts.log`.

`[ALERT] Entropy anomaly detected on Core 2 at 2025-11-10T09:32:14Z`

---

### Notes

- Requires elevated privileges for full sensor access
- Recommended for use in shielded or air-gapped environments
- Compatible with Linux-based systems only
