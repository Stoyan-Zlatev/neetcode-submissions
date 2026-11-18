class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for index, value in enumerate(temperatures):
            while stack and value > stack[-1][0]:
                curr_value, curr_index = stack.pop()
                result[curr_index] = index - curr_index
            stack.append((value, index))
        
            
        return result
