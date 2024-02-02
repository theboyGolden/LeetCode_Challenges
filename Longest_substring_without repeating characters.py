# Certainly! Here's a more complex Python coding task for you:

# **Task: Longest Substring Without Repeating Characters**

# Given a string, find the length of the longest substring without repeating characters.

# Function signature: `def length_of_longest_substring(s: str) -> int`

# **Example:**
# ```python
# s = "abcabcbb"
# result = length_of_longest_substring(s)
# print(result)
# ```
# Output:
# ```
# 3
# ```

# **Explanation:**
# The longest substring without repeating characters is "abc", which has a length of 3.

# **Constraints:**
# - The input string `s` consists of English letters, digits, symbols, and spaces.
# - The function should return an integer representing the length of the longest substring without repeating characters.

# Implement the `length_of_longest_substring` function to solve this task. This may involve using techniques such as the sliding window approach. Good luck!


def length_of_longest_substring(s: str) -> int:
    char_index = {}
    start = max_length = 0