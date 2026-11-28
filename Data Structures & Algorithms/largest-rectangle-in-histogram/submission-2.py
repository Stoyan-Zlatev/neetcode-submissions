class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_length = 0
        for index, height in enumerate(heights):
            curr_index = index
            curr_max = float('inf')
            while stack and stack[-1][0] >= height:
                curr_height, curr_index = stack.pop()
                curr_max = min(curr_max, curr_height)
                max_length = max((index - curr_index) * curr_max, max_length)
            max_length = max((index - curr_index + 1) * height, max_length)
            stack.append((height, curr_index))

        curr_max = float('inf')
        while stack:
            curr_height, curr_index = stack.pop()
            curr_max = min(curr_max, curr_height)
            max_length = max((len(heights) - curr_index) * curr_max, max_length)
        return max_length
