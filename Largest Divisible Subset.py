# 368. Largest Divisible Subset

# Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

# answer[i] % answer[j] == 0, or
# answer[j] % answer[i] == 0
# If there are multiple solutions, return any of them.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,2]
# Explanation: [1,3] is also accepted.
# Example 2:

# Input: nums = [1,2,4,8]
# Output: [1,2,4,8]
 

# Constraints:

# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 2 * 109
# All the integers in nums are unique.



def largestDivisibleSubset(nums):
    if not nums:
        return []
    
    nums.sort()
    n = len(nums)
    dp = [1] * n
    prev_index = [-1] * n
    max_length = 1
    max_index = 0


    for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev_index[i] = j
                    if dp[i] > max_length:
                        max_length = dp[i]
                        max_index = i
                        result = []
    while max_index != -1:
        result.append(nums[max_index])
        max_index = prev_index[max_index]

    return result[::-1]

# Test cases
nums1 = [1, 2, 3]
nums2 = [1, 2, 4, 8]

print(largestDivisibleSubset(nums1))  # Output: [1, 2] or [1, 3]
print(largestDivisibleSubset(nums2))  # Output: [1, 2, 4, 8]