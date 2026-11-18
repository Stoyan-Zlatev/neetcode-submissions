class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        def eval_operation(x: int, y: int, op: str) -> int:
            if op == '+':
                return x + y
            elif op == '-':
                return x - y
            elif op == '*':
                return x * y
            elif op == '/':
                return int(x / y)

        operators = ('+', '-', '*', '/')

        stack = []
        for token in tokens:
            if not token in operators:
                stack.append(int(token))
            else:
                y = stack.pop()
                x = stack.pop()
                stack.append(eval_operation(x, y, token))

        return stack[0]

    
        