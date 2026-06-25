class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, n in enumerate(nums):          
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if n + nums[left] + nums[right] < 0:
                    left += 1
                    continue
                elif n + nums[left] + nums[right] > 0:
                    right -= 1
                    continue
                else:
                    if [n, nums[left], nums[right]] not in result:
                        result.append([n, nums[left], nums[right]])
                left += 1
                right -= 1

        return result