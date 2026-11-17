class Solution:
    def isValid(self, s: str) -> bool:
        opposite = {')':'(', '}':'{', ']':'['}
        stack = []
        for bracket in s:
            if bracket in opposite:
                if stack and opposite[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)

        return stack == []