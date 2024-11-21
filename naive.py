def naive_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    positions = []

    # Traverse through the text
    for i in range(n - m + 1):
        # Check for a match
        if text[i:i + m] == pattern:
            positions.append(i)  # Record the starting index of match

    return positions

# Example usage
text = "ababcabcabababd"
pattern = "abc"
results = naive_string_match(text, pattern)

if not results:
    print(f"Pattern '{pattern}' not found in the text")
    
for result in results:
    print("Pattern found at positions:", result)
    
    