class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result = []

        for i, n in enumerate(sorted_nums):          
            left = i + 1
            right = len(sorted_nums) - 1

            while left < right:
                if n + sorted_nums[left] + sorted_nums[right] < 0:
                    left += 1
                    continue
                elif n + sorted_nums[left] + sorted_nums[right] > 0:
                    right -= 1
                    continue
                else:
                    if [n, sorted_nums[left], sorted_nums[right]] not in result:
                        result.append([n, sorted_nums[left], sorted_nums[right]])
                left += 1
                right -= 1

        return result