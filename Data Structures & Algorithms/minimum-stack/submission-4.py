class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_value = min(self.min_value, val)

    def pop(self) -> None:
        val = self.stack.pop()
        if not self.stack:
            self.min_value = float('inf')
        elif val == self.min_value:
            self.min_value = min(self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_value
        
        
