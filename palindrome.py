# 9. Palindrome Number
# Easy
# Topics
# Companies
# Hint
# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Check if the number is negative or ends with zero
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_number = 0
        original_number = x
        
        # Reverse the second half of the number
        while x > 0:
            digit = x % 10
            reversed_number = reversed_number * 10 + digit
            x //= 10

          # For a palindrome, the reversed number should match the original number
        return original_number == reversed_number