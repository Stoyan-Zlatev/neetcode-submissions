class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_length = 0
        for num in nums:
            if not (num - 1) in seen:
                curr_length = 1
                while num + curr_length in seen:
                    curr_length += 1
                max_length = max(max_length, curr_length)

        return max_length