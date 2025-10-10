import re
import time
import pyperclip

def detect_sensitive_data(text):
    patterns = {
        "Email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
        "IP Address": r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",
        "Credit Card": r"\b(?:\d[ -]*?){13,16}\b"
    }
    for label, pattern in patterns.items():
        if re.search(pattern, text):
            print(f"Suspicious {label} detected in clipboard!")

last_clipboard = ""

print("Monitoring clipboard... Press Ctrl+C to stop.")
try:
    while True:
        current = pyperclip.paste()
        if current != last_clipboard:
            detect_sensitive_data(current)
            last_clipboard = current
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopped.")
