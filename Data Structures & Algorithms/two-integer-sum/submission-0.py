# Understand:
#   - Find two indices i and j such that nums[i] + nums[j] == target
#   - Constraint, i != j
#   - Return the smaller index first
#   - Every input has exactly one pair of i and j
# Plan:
#   - Initialize a dictionary to store index's and numbers, ex map[index] = number
#   - Use a for loop to to go through each element in nums
#   - Calculate the difference between nums[i] and target to get value of nums[j]
#   - Check map if seen, if not store it in map, else return index of i and j


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement not in seen:
                seen[nums[i]] = i
            else:
                print(seen)
                return [min(seen[complement], i), max(seen[complement], i)]
        return []
        