# 279. Perfect Squares
# Medium
# Topics
# Companies
# Given an integer n, return the least number of perfect square numbers that sum to n.

# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

# Example 1:

# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
 

# Constraints:

# 1 <= n <= 104


import math

def numSquares(n):
    # Initialize dp array
    dp = [float('inf')] * (n + 1)
    dp[0] = 0


     # Iterate from 1 to n
    for i in range(1, n + 1):
        # Iterate through perfect squares less than or equal to i
        for j in range(1, int(math.sqrt(i)) + 1):
            # Update dp[i]
            dp[i] = min(dp[i], dp[i - j*j] + 1)
    
    return dp[n]

# Test cases
print(numSquares(12))  # Output: 3
print(numSquares(13))  # Output: 2