# 966. Divide Array Into Arrays With Max Difference
# Medium
# Topics
# Companies
# Hint
# You are given an integer array nums of size n and a positive integer k.

# Divide the array into one or more arrays of size 3 satisfying the following conditions:

# Each element of nums should be in exactly one array.
# The difference between any two elements in one array is less than or equal to k.
# Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.

 

# Example 1:

# Input: nums = [1,3,4,8,7,9,3,5,1], k = 2
# Output: [[1,1,3],[3,4,5],[7,8,9]]
# Explanation: We can divide the array into the following arrays: [1,1,3], [3,4,5] and [7,8,9].
# The difference between any two elements in each array is less than or equal to 2.
# Note that the order of elements is not important.
# Example 2:

# Input: nums = [1,3,3,2,7,3], k = 3
# Output: []
# Explanation: It is not possible to divide the array satisfying all the conditions.
 

# Constraints:

# n == nums.length
# 1 <= n <= 105
# n is a multiple of 3.
# 1 <= nums[i] <= 105
# 1 <= k <= 105


def divideArray(nums, k):
    n = len(nums)
    if n % 3 != 0:
        return []
    nums.sort()  # Sort the array in ascending order
    result = []

    for i in range(0, n, 3):
        group = [nums[i], nums[i + 1], nums[i + 2]]

        # Check the condition for the difference between any two elements in the group
        if group[2] - group[0] > k:
            return []

        result.append(group)
    return result

# Test the function with the provided examples
nums1, k1 = [1, 3, 4, 8, 7, 9, 3, 5, 1], 2
nums2, k2 = [1, 3, 3, 2, 7, 3], 3

output1 = divideArray(nums1, k1)
output2 = divideArray(nums2, k2)

print(output1)  # Output: [[1, 1, 3], [3, 4, 5], [7, 8, 9]]
print(output2)  # Output: []