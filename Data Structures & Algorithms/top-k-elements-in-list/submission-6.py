# Understand:
#   - Find the k most frequent elements in an array of integers
#   - Numbers may be returned in any order

# Plan:
#   - Initialize a dictionary to store number and its frequency
#   - Initailize a list, result
#   - For loop to iterate through array and store numbers in dict
#   - Key will be frequency, value will be number
#   - Use a while loop to iterate while count < k
#   - Use "max()" to find the max value in values and append key into result array
#   - Return result

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        seen = [[] for i in range(len(nums) + 1)]
        result = []
        count = 0

        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1

        for n, c in freq.items():
            seen[c].append(n)
        
        for i in range(len(seen) - 1, -1, -1):
            if seen[i]:
                for n in seen[i]:
                    result.append(n)
                    count += 1
            else:
                continue
            if count == k:
                return result





