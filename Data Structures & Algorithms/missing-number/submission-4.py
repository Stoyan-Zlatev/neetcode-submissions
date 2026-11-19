class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 0 1 2 3
        # 1 2 3
        n = len(nums)
        res= n
        for i in range(n):
            res += i - nums[i]

        return res
        


