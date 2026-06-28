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
        max_area = 0

        for i, height_1 in enumerate(heights):
            for j, height_2 in enumerate(heights):
                calculated_area = abs(j - i) * min(height_1, height_2)
                max_area = max(max_area, calculated_area)

        return max_area
        
        