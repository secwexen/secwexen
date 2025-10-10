function cleanJSON(input) {
  try {
    const parsed = JSON.parse(input);
    const cleaned = JSON.stringify(parsed, null, 2); // Pretty-print with 2-space indentation
    console.log("Cleaned JSON:\n", cleaned);
    return cleaned;
  } catch (error) {
    console.error("Invalid JSON:", error.message);
    return null;
  }
}

// Example usage
const raw = '{"name":"Arda","age":25,"skills":["Python","Cybersecurity"]}';
cleanJSON(raw);
