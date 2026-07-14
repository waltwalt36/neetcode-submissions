'''
Input: [1,2] or [1,5,7,9,0] or [10,9,8,1] or [1] or [1,10,0,8,0,2] or [2,10,0,12]

Sliding window, need two pointers
check if length is one return 0
Left = 0, right = 1
max_profit = 0
while r < len prices and l < len prices
    if right is greater than left:
        max_profit = max(right - left, max_profit)
    if right is less than left:
        move left to right
    right ++

return max_profit
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        left, right = 0, 1
        max_profit = 0

        while right < len(prices) and left < len(prices):
            if prices[right] > prices[left]:
                max_profit = max(prices[right] - prices[left], max_profit)
            if prices[right] < prices[left]:
                left = right
            right += 1
        return max_profit
