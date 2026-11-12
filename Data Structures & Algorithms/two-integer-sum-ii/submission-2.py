class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for index, number in enumerate(numbers):
            if number in seen:
                return [seen[number] + 1, index + 1]
            diff = target - number
            seen[diff] = index