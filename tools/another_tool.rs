// another_tool.rs
// Entropy Drift Analyzer for Air-Gapped Systems
// Author: [X99874]
// License: GPL-3.0 license

use std::fs;
use std::thread;
use std::time::{Duration, SystemTime};
use std::collections::VecDeque;

/// Configuration parameters
const SAMPLE_INTERVAL_MS: u64 = 100;
const WINDOW_SIZE: usize = 64;
const ENTROPY_THRESHOLD: f64 = 0.72;

/// Reads raw CPU telemetry from /proc/stat
fn read_cpu_entropy() -> Option<f64> {
    let contents = fs::read_to_string("/proc/stat").ok()?;
    let line = contents.lines().next()?;
    let values: Vec<u64> = line
        .split_whitespace()
        .skip(1)
        .filter_map(|v| v.parse::<u64>().ok())
        .collect();

    let sum: u64 = values.iter().sum();
    let entropy = if sum > 0 {
        let normalized: Vec<f64> = values.iter().map(|&v| v as f64 / sum as f64).collect();
        -normalized.iter().map(|&p| p * p.log2()).sum::<f64>()
    } else {
        0.0
    };

    Some(entropy)
}

/// Main monitoring loop
fn monitor_entropy() {
    let mut window: VecDeque<f64> = VecDeque::with_capacity(WINDOW_SIZE);

    loop {
        if let Some(entropy) = read_cpu_entropy() {
            window.push_back(entropy);
            if window.len() > WINDOW_SIZE {
                window.pop_front();
            }

            if window.len() == WINDOW_SIZE {
                let avg: f64 = window.iter().copied().sum::<f64>() / WINDOW_SIZE as f64;
                if entropy < avg * ENTROPY_THRESHOLD {
                    let timestamp = SystemTime::now();
                    println!(
                        "[ALERT] Entropy drift detected: {:.4} at {:?}",
                        entropy, timestamp
                    );
                }
            }
        }

        thread::sleep(Duration::from_millis(SAMPLE_INTERVAL_MS));
    }
}

fn main() {
    println!("Starting entropy drift monitor...");
    monitor_entropy();
}
