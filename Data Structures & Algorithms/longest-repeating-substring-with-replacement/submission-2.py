'''
Input: "XYYX" k = 2, "AAABABB" k = 1, "" k = 0, "" k = 1, "AAA" k = 2, "ABBBBA" k = 5
        "ABABABA" k = 3

Game Plan:
    Intialize left and right pointers
    Dictionary to keep track of frequency
    Intialize variables for maxFreq and maxWin
    Move right pointer only if the window size - max frequency is <= k
    Else move the left pointer foward and remove current letter from dictionary
    Return maxWin
    '''
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        left, maxFreq, maxWin = 0, 0, 0

        for right in range(len(s)):
            freq[s[right]] += 1

            maxFreq = max(freq[s[right]], maxFreq)
            
            while right - left + 1 - maxFreq > k:
                freq[s[left]] -= 1
                left += 1

            maxWin = max(maxWin, right - left + 1)

        return maxWin            