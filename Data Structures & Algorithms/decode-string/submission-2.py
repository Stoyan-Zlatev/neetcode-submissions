class Solution:
    def decodeString(self, s: str) -> str:
        curr_str = ""
        curr_num = 0
        stack = []

        for symbol in s:
            if symbol == '[':
                stack.append(curr_str)
                stack.append(curr_num)
                curr_num = 0
                curr_str = ""
            elif symbol == ']':
                num = stack.pop()
                prev_str = stack.pop()
                curr_str = prev_str + (curr_str * num)
            elif symbol.isdigit():
                curr_num = curr_num * 10 + int(symbol)
            else:
                curr_str += symbol

        return curr_str