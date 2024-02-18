class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Initialize dictionaries to store character counts
        count_s = {}
        count_t = {}
        
        # Count characters in string s
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        
        # Count characters in string t
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
        
        # Compare counts to find the extra letter
        for char in count_t:
            if char not in count_s or count_t[char] > count_s[char]:
                return char

# Example usage
solution = Solution()
result = solution.findTheDifference("abcd", "abcde")
print(result)  # Output: "e"
