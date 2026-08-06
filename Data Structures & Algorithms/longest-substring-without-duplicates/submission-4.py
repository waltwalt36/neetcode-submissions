'''
Input: "zxyzxyz" or "" or "xxxx" or "abcde" or "acacac" or "12312345" or "a" or "dvdf" or ""

check if not str return 0
check if str len is 1 return 1
left and right pointer, 0 and 1
variable max_substring_length to keep track of max length of longest substring
Need a set to keep track of unique characters
start off by putting the first character in the set

while left < str len and right < str len:
    if right not in set
        add right to set
        max_substring_length = max(length of set, max_substring_length)
        right += 1
    else:
        max_substring_length = max(length of set, max_substring_length)
        clear set
        move left pointer to right
        add left to set
        right += 1

return max_length
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        max_length = 0
        duplicates = {}

        if not s:
            return max_length

        while right < len(s):
            if s[right] not in duplicates:
                duplicates[s[right]] = right
                right += 1
                max_length = max(len(s[left:right]), max_length)
            else:
                if duplicates[s[right]] >= left:
                    left = duplicates[s[right]] + 1
                    duplicates.pop(s[right])
                else:
                    duplicates[s[right]] = right
                    right += 1
                    max_length = max(len(s[left:right]), max_length)

        return max_length
               





