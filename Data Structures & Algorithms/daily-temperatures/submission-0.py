class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[0],0)]
        result = [0] * len(temperatures)
        for index in range(1, len(temperatures)):
            curr_value = temperatures[index]
            while stack and curr_value > stack[-1][0]:
                value, curr_index = stack.pop()
                result[curr_index] = index - curr_index
            stack.append((curr_value, index))
        
            
        return result
