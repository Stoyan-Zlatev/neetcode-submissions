class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)
        left = [1] * (nums_length + 1)
        right = [1] * (nums_length + 1)

        for i in range(1, nums_length+1):
            left[i] = nums[i - 1] * left[i-1]

        for i in range(nums_length-1, -1, -1):
            right[i] = nums[i] * right[i+1]

        result = []
        for i in range(nums_length):
            result.append(left[i] * right[i+1])

        return result