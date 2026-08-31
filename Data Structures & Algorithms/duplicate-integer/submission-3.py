class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = defaultdict(int)
        for num in nums:
            if seen[num]:
                return True
            seen[num] = True
        return False