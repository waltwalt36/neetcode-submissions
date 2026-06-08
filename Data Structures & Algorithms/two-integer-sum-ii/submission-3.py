class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        if len(numbers) < 2:
            return numbers

        while left < right:
            value = numbers[left] + numbers[right]

            if value == target:
                return [left + 1, right + 1]
            elif value < target:
                left += 1
            else:
                right -= 1
                
        return []

                    