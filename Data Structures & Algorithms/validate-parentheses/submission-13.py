'''
    Stack implementation
    Use a dictionary to pair closing brackets with their corresponding open brackets
    Use for loop to iterate through s
    Check if character in s is a key in dictionary pairs, if it is not append character to stack
    If character is a key in pairs then pop top of stack and check that it is corresponding open bracket
    If it is not then return False
    After the loop if s is valid return True

    edge cases:
        "" = True
        "[" = False
        "[[[" = False
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")" : "(", "}" : "{", "]" : "["}

        for c in s:
            if c not in pairs:
                stack.append(c)
            else:
                open_bracket = stack.pop() if stack else ""
                
                if open_bracket != pairs[c]:
                    return False

        return len(stack) == 0