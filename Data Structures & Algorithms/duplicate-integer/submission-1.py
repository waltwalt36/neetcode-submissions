class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = {}   

        for n in nums:
            if n not in duplicates:
                duplicates[n] = 1
            else:
                return True
        return False