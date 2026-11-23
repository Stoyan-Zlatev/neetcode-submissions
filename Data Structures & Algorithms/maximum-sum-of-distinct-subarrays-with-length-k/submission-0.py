class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = float('-inf')
        seen = set()
        counter = defaultdict(int)
        curr_sum = 0
        for index in range(k):
            curr_sum += nums[index]
            seen.add(nums[index])
            counter[nums[index]] += 1

        if len(seen) == k:
            max_sum = curr_sum


        for i in range(k, len(nums)):
            counter[nums[i - k]] -= 1
            if counter[nums[i - k]] == 0:
                seen.remove(nums[i - k])
            curr_sum -= nums[i - k]
            curr_sum += nums[i]
            seen.add(nums[i])
            counter[nums[i]] += 1
            if len(seen) == k:
                max_sum = max(max_sum, curr_sum)

        return max_sum if max_sum > float('-inf') else 0
