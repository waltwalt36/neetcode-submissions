# Understand:
# - Given two strings
# - Return true if the two strings are anagrams otherwise return false
# - An anagram is a string that contains the same characters as another but can be in diff order
# Plan:
# - Initilaze two dictionaries
# - Use dictionary to store letters and the amount of times they appear
# - Compare dictionaries, if amount of letters matches for both return True else return False
# Implement:
# dictionary_s = {}
# dictionary_t = {}
# for c in s:
#   if c in dictionary_s:
#       dictionary_s[c] += 1
#   else:
#       dictionary_s[c] = 1
# for c in t:
#   if c in dictionary_t:
#       dictionary_t[c] += 1
#   else:
#       dictionary_t[c] = 1
# tuple_s = tuple(dictionary_s)
# tuple_t = tuple(dictionary_t)
# for i in range(min(tuple_s, tuple_t))
#   if tuple_s[i] != tuple_t[i]:
#       return False
# return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary_s = {}
        dictionary_t = {}

        for c in s:
            if c in dictionary_s:
                dictionary_s[c] += 1
            else:
                dictionary_s[c] = 1
        for c in t:
            if c in dictionary_t:
                dictionary_t[c] += 1
            else:
                dictionary_t[c] = 1

        if dictionary_s == dictionary_t:
            return True
        return False
        