# 451. Sort Characters By Frequency
# Medium
# Topics
# Companies
# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.

 

# Example 1:

# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:

# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:

# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
 

# Constraints:

# 1 <= s.length <= 5 * 105
# s consists of uppercase and lowercase English letters and digits.


def frequencySort(s):
    char_frequency = {}
    
    # Count the frequency of each character in the string
    for char in s:
        char_frequency[char] = char_frequency.get(char, 0) + 1
    # Sort the characters based on their frequency in decreasing order
    sorted_chars = sorted(char_frequency.keys(), key=lambda x: char_frequency[x], reverse=True)
    
    # Construct the sorted string
    sorted_string = ''.join(char * char_frequency[char] for char in sorted_chars)
    
    return sorted_string

# Test the function with the provided examples
s1 = "tree"
s2 = "cccaaa"
s3 = "Aabb"

output1 = frequencySort(s1)
output2 = frequencySort(s2)
output3 = frequencySort(s3)

print(output1)  # Output: "eert"
print(output2)  # Output: "aaaccc"
print(output3)  # Output: "bbAa"
