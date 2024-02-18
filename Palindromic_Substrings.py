# 647. Palindromic Substrings
# Medium
# Topics
# Companies
# Hint
# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

 

# Example 1:

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of lowercase English letters.


def countSubstrings(s: str) -> int:
    def expandAroundCenter(left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
    count = 0
    for i in range(len(s)):
        # Case 1: Odd-length palindromes
        count += expandAroundCenter(i, i)
        # Case 2: Even-length palindromes
        count += expandAroundCenter(i, i + 1)
    return count

# Test cases
s1 = "abc"
s2 = "aaa"

print(countSubstrings(s1))  # Output: 3
print(countSubstrings(s2))  # Output: 6