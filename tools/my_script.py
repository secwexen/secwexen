# my_script.py
# Acoustic Signal Profiler for Covert Channel Detection
# Author: [X99874]
# License: GPL-3.0 license

import pyaudio
import numpy as np
import json
import argparse
from datetime import datetime

# Configuration defaults
DEFAULT_DURATION = 30  # seconds
DEFAULT_SENSITIVITY = 'high'
DEFAULT_OUTPUT = None  # stdout

# Frequency bands of interest (in Hz)
FREQUENCY_BANDS = {
    'low': (1000, 5000),
    'medium': (5000, 10000),
    'high': (10000, 20000)
}

def capture_audio(duration: int, rate: int = 44100, chunk: int = 1024) -> np.ndarray:
    """Capture raw audio data from the default microphone."""
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=rate,
                        input=True,
                        frames_per_buffer=chunk)

    frames = []
    for _ in range(int(rate / chunk * duration)):
        data = stream.read(chunk, exception_on_overflow=False)
        frames.append(np.frombuffer(data, dtype=np.int16))

    stream.stop_stream()
    stream.close()
    audio.terminate()

    return np.concatenate(frames)

def analyze_spectrum(signal: np.ndarray, rate: int, sensitivity: str) -> dict:
    """Perform FFT and extract dominant frequencies."""
    fft_result = np.fft.rfft(signal)
    freqs = np.fft.rfftfreq(len(signal), d=1/rate)
    magnitude = np.abs(fft_result)

    band = FREQUENCY_BANDS.get(sensitivity, FREQUENCY_BANDS['high'])
    indices = np.where((freqs >= band[0]) & (freqs <= band[1]))[0]

    dominant_freqs = freqs[indices][np.argsort(magnitude[indices])[-3:]].tolist()
    anomaly_score = float(np.std(magnitude[indices]) / np.mean(magnitude[indices]))

    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "dominant_frequencies": [round(f, 2) for f in dominant_freqs],
        "anomaly_score": round(anomaly_score, 2)
    }

def main():
    parser = argparse.ArgumentParser(description="Acoustic Signal Profiler")
    parser.add_argument("--duration", type=int, default=DEFAULT_DURATION, help="Recording duration in seconds")
    parser.add_argument("--sensitivity", choices=["low", "medium", "high"], default=DEFAULT_SENSITIVITY, help="Detection sensitivity")
    parser.add_argument("--output", type=str, help="Path to output JSON file")

    args = parser.parse_args()

    print(f"[INFO] Capturing audio for {args.duration} seconds...")
    signal = capture_audio(args.duration)
    print("[INFO] Analyzing spectrum...")
    result = analyze_spectrum(signal, rate=44100, sensitivity=args.sensitivity)

    if args.output:
        with open(args.output, 'w') as f:
            json.dump(result, f, indent=2)
        print(f"[INFO] Results saved to {args.output}")
    else:
        print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
