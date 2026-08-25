'''
Stack problem
Push each number into stack
If we reach an opperand pop stack until its empty and save numbers
Do operation and then push the result back into the stack
Push numbers again until opperand then repeat process until end of string
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ["+", "-", "*", "/"]

        for t in tokens:
            if t not in operands:
                stack.append(int(t))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if t == "+":
                    stack.append(num1 + num2)
                elif t == "-":
                    stack.append(num1 - num2)
                elif t == "*":
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1 / num2))
        return stack[0]