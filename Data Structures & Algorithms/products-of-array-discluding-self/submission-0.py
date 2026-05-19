# Understand:
#   - Return an array output where output[i] is the product of all the elements in nums except nums[i]
#   - Product is guaranteed to fit in a 32-bit integer (8 bytes)
#   - Solve in O(n) without using the dicision operator

# Plan:
#   - Create an array output, to store results
#   - Initialize a map to store values
#   - {key = i, value = nums[i]}
#   - Store all nums in map
#   - Loop through each element in nums and look up in map
#   - Multiply all elements no equal to current element with O(1) lookup
#   - Append result to output array
#   - Return output

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        temp = {}

        for i in range(len(nums)):
            temp[i] = nums[i] # {index : nums[i]}

        for i in range(len(nums)):
            product = 1
            for key, value in temp.items():
                if i != key:
                    product *= value
            output.append(product)
            
        return output

