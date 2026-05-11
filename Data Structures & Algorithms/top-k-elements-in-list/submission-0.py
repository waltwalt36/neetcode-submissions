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
        seen = {}
        result = []
        count = 0

        for n in nums:

            if n not in seen:
                seen[n] = 1
            else:
                seen[n] += 1
            
            if n in freq.values():
                freq.values().remove(n)

            if seen[n] not in freq:    
                freq[seen[n]] = [n]
            else:
                freq[seen[n]].append(n)

        freq_list = list(freq.items())
        print(freq_list)
        
        while count < k:
            last = len(freq_list) - 1
            if freq_list[last][1]: 
                max_value = max(freq_list[last][1])
                if max_value in result:
                    freq_list[last][1].remove(max_value)
                    continue
                result.append(max_value)
                freq_list[last][1].remove(max_value)
                count += 1
            else:
                freq_list.pop(last)
        
        return result





