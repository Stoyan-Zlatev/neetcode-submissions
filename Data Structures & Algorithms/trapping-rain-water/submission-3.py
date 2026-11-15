class Solution:
    def trap(self, height: List[int]) -> int:
        height_length = len(height)

        if height_length <= 1:
            return 0
        prefix = [0] * height_length
        suffix = [0] * height_length
        for i in range(1, height_length):
            prefix[i] = max(prefix[i - 1], height[i - 1])
            suffix[height_length - 1 - i] = max(suffix[height_length - i], height[height_length - i])

        total_water = 0
        for i in range(height_length):
            curr_water = min(prefix[i], suffix[i]) - height[i]
            if curr_water > 0:
                total_water += curr_water

        return total_water

            
            