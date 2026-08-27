'''
    Stack question
    Test Case:  [] or [22, 21, 20] or [30, 38, 30, 36, 35, 40, 28] or [1, 2, 3, 4]
                [31, 30, 29, 28, 40]

    Idea is to use a stack to keep track of seen temps
    When on the ith day a higher temp is found take the current temp and subract by all the previous temps
    Subtract starting from the beginneing of the stack and append to result
    iterate through array until all numbers have been accounted for
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)
                continue
            if temperatures[stack[-1]] >= temperatures[i]:
                stack.append(i)
            else:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    result[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
        return result