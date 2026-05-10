# Understand:
#   - Group together all anagrams in array of strings strs
#   - Return an array of arrays, each with corresponding grouped anagrams
#   - An anagram is a string that contains the same letters but different order
#   - Strings consist of lowercase letters only

# Plan:
#   - Initlaize an array, result to store grouped anagrams
#   - Initialize a dictionary to store a key and array of grouped anagrams with that key
#   - Key string in alphabetical order
#   - Return all the values of dictonary to result and return result

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anagrams = {}

        for s in strs:
            key = "".join(sorted(s))

            if key not in anagrams:
                anagrams[key] = [s]
            else:
                anagrams[key].append(s)
        
        for value in anagrams.values():
            result.append(value)

        return result
        