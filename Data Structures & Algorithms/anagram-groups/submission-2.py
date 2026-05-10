# Understand:
#   - Group together all anagrams in array of strings strs
#   - Return an array of arrays, each with corresponding grouped anagrams
#   - An anagram is a string that contains the same letters but different order
#   - Strings consist of lowercase letters only

# Plan:
#   - Initlaize an array, result to store grouped anagrams
#   - Initialize a dictionary to store a key and array of grouped anagrams with that key
#   - Initialize an array to store a unique key
#   - Use a nested for loop to go through each character and create key
#   - Algorithm for calculating key is ordinal value of current chracter minus ordinal value of 'a'
#   - Return all the values of dictonary to result and return result

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anagrams = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            key = " ".join(map(str, count))

            if key not in anagrams:
                anagrams[key] = [s]
            else:
                anagrams[key].append(s)
        
        for value in anagrams.values():
            result.append(value)

        return result
        