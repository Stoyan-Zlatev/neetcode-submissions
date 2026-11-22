class Solution:
    def trap(self, height: List[int]) -> int:
        postfix = [0] * len(height)
        curr_max = 0
        for i in range(len(height) -1, -1, -1):
            curr_max = max(curr_max, height[i])
            postfix[i] = curr_max

        curr_max = 0
        result = 0
        for i in range(len(height)):
            curr_max = max(curr_max, height[i])
            result += min(curr_max, postfix[i]) - height[i]

        return result