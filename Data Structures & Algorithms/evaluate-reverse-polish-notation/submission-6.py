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
        result = tokens[0]
        for token in tokens:
            if not token in operators:
                stack.append(token)
            else:
                y = stack.pop()
                x = stack.pop()
                result = eval_operation(int(x), int(y), token)
                
                stack.append(result)

        return result

    
        