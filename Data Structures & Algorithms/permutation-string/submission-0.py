'''
    Sliding window problem
    Set window size to the length of s1
    Two dictionaries, one is refrence dictionary that contains s1 and its frequencies the other to keep track of current window
    Add current window to frequencie dictionary for current window
    Use a for loop to move right pointer each iteration
    Add the right pointers value to current window freq dictionary
    Check if refrence dict and curr win dict are equal, if so return true
    if not then remove left value from current win freq dict and move left foward one
    After for loop return False if permutation not found
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, len(s1) - 1
        reference = {}
        current_window = {}

        for c in s1:
            if c not in reference:
                reference[c] = 1
            else:
                reference[c] += 1
        
        for i in range(right):
            if s2[i] not in current_window:
                current_window[s2[i]] = 1
            else:
                current_window[s2[i]] += 1
        print(current_window)

        for right in range(right, len(s2)):
            if s2[right] not in current_window:
                current_window[s2[right]] = 1
            else:
                current_window[s2[right]] += 1
            print(right)
            print(current_window)
            #print(reference)
            #print(current_window)
            #print()
            if reference == current_window:
                return True
            
            current_window[s2[left]] -= 1

            if current_window[s2[left]] == 0:
                del current_window[s2[left]]
            left += 1
        
        return False