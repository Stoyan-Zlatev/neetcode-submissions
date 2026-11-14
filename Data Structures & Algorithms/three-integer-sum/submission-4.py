class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        seen = set()
        for index, num in enumerate(nums):
            if num > 0:
                break
            l, r = index + 1, len(nums) - 1
            while l < r:
                curr_sum = -(nums[l] + nums[r])
                if curr_sum == num:
                    if not (num, nums[l], nums[r]) in seen:
                        result.append([num, nums[l], nums[r]])
                        seen.add((num, nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif curr_sum < num:
                    r -= 1
                else: 
                    l += 1
        
        return result