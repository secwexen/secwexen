# Entropy Detector

This tool calculates the entropy of a given string — a measure of randomness and unpredictability.  
It's commonly used in cybersecurity to evaluate the strength of passwords, tokens, API keys, or any sensitive data.

## What is Entropy?

Entropy quantifies how unpredictable a string is.  
Higher entropy means the string is harder to guess or brute-force.

- Low entropy → predictable, weak
- High entropy → random, strong

## File Location

tools/entropy_detector.py

## Usage

```bash
python tools/entropy_detector.py
```

## Example Output

Enter a string to analyze: Arda123!@#
Entropy: 3.42 bits

## Cybersecurity Use Cases

- Password strength analysis
- Token randomness validation
- Detecting hardcoded secrets
- Evaluating session IDs or JWTs

## Disclaimer

This tool is intended for educational and ethical use only.
Do not use it to analyze or extract unauthorized data.
