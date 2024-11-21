def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m # Initializes LPS array with zeros
    length = 0 # Tracks length of the current matching prefix and suffix.
    i = 1

    while i < m:
        if pattern[i] == pattern[length]: # a match is found
            length += 1
            lps[i] = length # Increment length and assign it to lps[i]
            i += 1 # Move to the next character
        else:
            if length != 0:
                length = lps[length - 1] # reset length to lps[length - 1] (backtrack)
            else:
                lps[i] = 0
                i += 1
                
    return lps

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    positions = []
    
    i = j = 0
    while i < n:
        if pattern[j] == text[i]: # match found, increment both indices
            i += 1
            j += 1
        
        if j == m: # (end of pattern)
            positions.append(i - j)  # Match found, add i - j (starting index of the match) to positions
            j = lps[j - 1] # Reset j using the LPS array
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1] # backtrack using the LPS array
            else:
                i += 1 # increment i to move forward in the text
                
    return positions

# Example usage
text = "ababcabcabababd"
patterns = ["ababc", "abb", "aba", "bcab"]
for pattern in patterns:
    result = kmp_search(text, pattern)
    if result:
        for pos in result:
            print(f"Found '{pattern}' at index {pos}")
    else:
        print(f"Pattern '{pattern}' not found in the text")
        
        
