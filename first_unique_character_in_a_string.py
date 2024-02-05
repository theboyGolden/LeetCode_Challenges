# 387. First Unique Character in a String

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only lowercase English letters.

def firstUniqChar(s):
    char_frequency = {}

    # Count the frequency of each character in the string
    for char in s:
        char_frequency[char] = char_frequency.get(char, 0) + 1
        # Iterate through the string to find the first unique character
    for i, char in enumerate(s):
        if char_frequency[char] == 1:
            return i
        # If no unique character is found, return -1
    return -1

# Test the function with the provided examples
s1 = "leetcode"
s2 = "loveleetcode"
s3 = "aabb"