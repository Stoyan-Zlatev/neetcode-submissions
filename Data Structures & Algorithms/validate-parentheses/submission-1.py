class Solution:
    def isValid(self, s: str) -> bool:
        opposite = {')':'(', '}':'{', ']':'['}
        stack = []
        for bracket in s:
            if bracket not in opposite:
                stack.append(bracket)
            else:
                if not stack or not opposite[bracket] == stack[-1]:
                    return False
                stack.pop()

        return stack == []