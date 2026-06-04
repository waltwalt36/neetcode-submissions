# Gameplan:
#   - Initalize two pointers, left and right
#   - While right is greater than left and character isAlpha() keep moving the left and right pointers
#   - Check if left and right are equal, if so continue if not then return false
#   - Return true after while loop

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while right > left:
            if not s[left].isalnum():
                print("Increase left")
                left += 1
                continue
            if not s[right].isalnum():
                print("Decrease right")
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True 