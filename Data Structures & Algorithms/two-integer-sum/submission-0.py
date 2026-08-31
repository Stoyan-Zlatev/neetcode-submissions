class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = defaultdict(int)
        for index,number in enumerate(nums):
            diff = target - number
            if diff in indexes:
                return [indexes[diff], index]
            indexes[number]=index

        return False
