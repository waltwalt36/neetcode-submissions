# plan:
#   - Store all nums in the set for O(1) lookups
#   - Loop through nums list O(n)
#   - Identify the start of a sequence which is any number that doesn't have a value n - 1 stored already in the set
#   - Check for sequence and then store sequence in a variable
#   - Then return variable sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        sequence = 0

        for n in nums:
            if (n - 1) not in numbers:
                current = n
                miniSeq = 0
                while(current in numbers):
                    current += 1
                    miniSeq += 1
                sequence = max(miniSeq, sequence)
        return sequence


        
        
                