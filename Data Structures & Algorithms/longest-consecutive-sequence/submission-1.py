# plan:
#   - scan all elements and store inside of a hash set
#   - { num }
#   - Range based for loop range(min(nums), max(nums) + 1)
#   - number to keep track of longest consec. seq.
#   - If statement to check for a consec. seq.
#   -

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        count = 0
        consecutive = []

        if len(nums) == 0:
            return 0
            
        for i in range(min(nums), max(nums) + 1):
            if i in seq:
                count += 1
            else:
                consecutive.append(count)
                count = 0

        consecutive.append(count)
        return max(consecutive)