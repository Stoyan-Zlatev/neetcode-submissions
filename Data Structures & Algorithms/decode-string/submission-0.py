class Solution:
    def decodeString(self, s: str) -> str:
        curr_string = ""
        curr_number = ""
        stack = []
        form = 0
        result = ""
        index = 0
        while not s[index].isdigit():
            result += s[index]
            index += 1

        for i in range(index, len(s)):
            symbol = s[i]
            if symbol.isdigit():
                if curr_string:
                    stack.append(curr_string)
                    curr_string = ""
                curr_number += symbol
            elif symbol == '[':
                stack.append(curr_number)
                form += 1
                curr_number = ""
            elif symbol == ']':
                form -= 1
                number = int(stack.pop())
                curr_string *= number
                if form == 0:
                    result += curr_string
                    curr_string = ""
                else:
                    if not stack[-1].isnumeric():
                        curr_string = stack[-1] + curr_string
                        stack.pop()
            else:
                curr_string += symbol

        return result+curr_string