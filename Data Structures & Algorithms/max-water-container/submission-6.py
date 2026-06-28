'''
Want our solution to have as long of a width as possible
between both bars

We also want the bars with the tallest heights to maximize
the area of the container

Using two pointers we want to calculate the area between
both pointers and store in some variable calculated_area

To calculate the area we want to use the equation
area = (right - left) * min(nums[left], nums[right])

Check if calculated_area is greater than max_area

    if yes update max_area == calculated area

    else do nothing

Then we want to update pointers but we want to do it in
a smart way

Set up a condition to check if nums[left + 1] and 
nums[right - 1] are greater than the current values at the 
left and right pointers

    if this is the case move the update respective pointer

    else just move both pointers
'''
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0

        while left < right:
            calculated_area = (right - left) * min(heights[left], heights[right])
            max_area = max(max_area, calculated_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
    
        return max_area
        