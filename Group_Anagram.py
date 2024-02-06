# 49. Group Anagrams
# Medium
# Topics
# Companies
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.



def groupAnagrams(strs):
    anagrams = {}
    
    # Iterate through each word in the input array
    for word in strs:
        # Sort the characters of the word and use it as a key in the dictionary
        sorted_word = ''.join(sorted(word))

         # If the sorted word is already in the dictionary, append the word to its list of anagrams
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            # Otherwise, create a new entry in the dictionary with the sorted word as the key
            anagrams[sorted_word] = [word]
    
    # Convert the values of the dictionary to a list and return the result
    return list(anagrams.values())