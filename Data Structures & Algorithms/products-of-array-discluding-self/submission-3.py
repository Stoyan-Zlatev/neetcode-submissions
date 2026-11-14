class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)
        result = [1] * nums_length

        #Prefix run
        for i in range(1, nums_length):
            result[i] = nums[i-1] * result[i-1]

        #Postfix run

        postfix = 1
        for i in range(nums_length - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result

