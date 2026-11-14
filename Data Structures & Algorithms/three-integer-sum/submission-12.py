class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for index, num in enumerate(nums):
            if num > 0:
                break
            if index > 0 and num == nums[index - 1]:
                continue
            l, r = index + 1, len(nums) - 1
            while l < r:
                curr_sum = -(nums[l] + nums[r])
                if curr_sum == num:
                    result.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif curr_sum < num:
                    r -= 1
                else: 
                    l += 1
        
        return result