class Solution:
    def trap(self, height: List[int]) -> int:
        postfix = [0] * len(height)
        postfix[- 1] = height[len(height) - 1]
        for i in range(len(height) - 2, -1, -1):
            postfix[i] = max(height[i], postfix[i + 1])
        left = 0
        left_max = 0
        result = 0
        for i in range(len(height)):
            left_max = max(left_max, height[i])
            result += min(postfix[i], left_max) - height[i]

        return result