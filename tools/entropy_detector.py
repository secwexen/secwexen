import math

def calculate_entropy(text):
    if not text:
        return 0
    freq = {char: text.count(char) / len(text) for char in set(text)}
    entropy = -sum(p * math.log2(p) for p in freq.values())
    return round(entropy, 2)

# Example usage
sample = "USER!@#"
print(f"Entropy: {calculate_entropy(sample)} bits")
