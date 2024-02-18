# # You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# # Return the merged string.

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
 

# Constraints:

# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ""
        i, j = 0, 0
        
        while i < len(word1) and j < len(word2):
            result += word1[i] + word2[j]
            i += 1
            j += 1
        
        # Append the remaining characters from word1, if any
        result += word1[i:]
        
        # Append the remaining characters from word2, if any
        result += word2[j:]
        
        return result

# Example usage:
solution = Solution()
output1 = solution.mergeAlternately("abc", "pqr")
output2 = solution.mergeAlternately("ab", "pqrs")
output3 = solution.mergeAlternately("abcd", "pq")

print(output1)  # Output: "apbqcr"
print(output2)  # Output: "apbqrs"
print(output3)  # Output: "apbqcd"
