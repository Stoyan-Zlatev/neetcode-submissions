class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * (len(nums) + 1)
        right = [1] * (len(nums) + 1)
        for index, num in enumerate(nums):
            left[index + 1] = left[index] * num
            right[len(nums) - 1 - index] = right[len(nums) - index] * nums[len(nums) - 1 - index]

        result = []
        for i in range(1, len(nums) + 1):
            result.append(left[i-1] * right[i])

        return result


