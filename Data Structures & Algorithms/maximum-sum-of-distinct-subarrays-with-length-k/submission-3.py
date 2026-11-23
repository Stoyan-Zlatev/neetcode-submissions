class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = float('-inf')
        counter = {}
        curr_sum = 0
        for index in range(k):
            curr_sum += nums[index]
            counter[nums[index]] = counter.get(nums[index], 0) + 1

        if len(counter) == k:
            max_sum = curr_sum


        for i in range(k, len(nums)):
            counter[nums[i - k]] -= 1
            if counter[nums[i - k]] == 0:
                del counter[nums[i - k]]
            curr_sum -= nums[i - k]
            curr_sum += nums[i]
            counter[nums[i]] = counter.get(nums[i], 0) + 1
            if len(counter) == k:
                max_sum = max(max_sum, curr_sum)

        return max_sum if max_sum > float('-inf') else 0
