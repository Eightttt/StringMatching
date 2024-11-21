# Create a dictionary to map letters to their corresponding values
alphabet_set = {chr(i + 96): i for i in range(1, 27)}  # a to z is 1 to 26

def rabin_karp(text, pattern, p, m):
    def get_alphabet_value(alpha):
        return alphabet_set[alpha]  # Get value from alphabet set
    
    def hash(s, length):
        hash_value = 0
        for i in range(length):
            # Calculate hash value for each letter in string
            hash_value = hash_value + (get_alphabet_value(s[i]) * p**(length - i - 1))
        hash_value = hash_value % m
        return hash_value

    n = len(text)
    results = []

    pattern_length = len(pattern)  # Get length of current pattern
    pattern_hash = hash(pattern, pattern_length)  # Hash of current pattern
    text_hash = hash(text, pattern_length)  # Hash of initial substring of text
    
    for i in range(n - pattern_length + 1):
        # Check if hash matches
        if text_hash == pattern_hash:
            # If hash matches, check for actual substring match
            if text[i:i + pattern_length] == pattern:
                results.append(i)

        # Calculate hash for next substring
        if i < n - pattern_length:
            # Rolling hash calculation
            text_hash = ((text_hash - (get_alphabet_value(text[i]) * (p ** (pattern_length-1))))
                         * p + get_alphabet_value(text[i + pattern_length])) % m
            
            # Ensure text_hash is non-negative
            text_hash = (text_hash + m) % m

    return results

# Example usage
text = "ababcabcabababd"
patterns = ["abc", "ab", "abz"]
for pattern in patterns:
    results = rabin_karp(text, pattern, 26, 2**32)
    if results:
        for result in results:
            print(f"Found '{pattern}' at index {result}")
    else:
        print(f"Pattern '{pattern}' not found in the text")
    

