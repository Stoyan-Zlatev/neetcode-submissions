class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(0, heights[0])]
        max_area = 0
        for i in range(1, len(heights)):
            curr_index = i
            while stack and heights[i] < stack[-1][1]:
                curr_index, curr_height = stack.pop()
                area = curr_height * (i-curr_index)
                max_area = max(max_area, area)
            stack.append((curr_index, heights[i]))

        while stack:
            curr_index, curr_height = stack.pop()
            area = curr_height * (len(heights)-curr_index)
            max_area = max(max_area, area)

        return max_area
