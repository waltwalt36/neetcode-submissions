# plan:
#   - Initalize an output array
#   - Use a for loop to iterate through nums fowards
#   - Calculate prefix product, product = 1
#   - For the first value just append 1 to current index
#   - Subsequent values fill in with prefix product
#   - For loop to iterate through nums backwards
#   - Obviously first index just times 1
#   - then subsequent values fill in with postfix product

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        output.append(1)

        product = 1
        for i in range(1, len(nums)):
            product *= nums[i - 1]
            output.append(product)
        
        print(output)
        product = 1
        for i in range(len(nums) - 2, -1, -1):
            product *= nums[i + 1]
            output[i] *= product
        
        return output