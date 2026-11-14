class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        tops = defaultdict(list)
        for key, value in counter.items():
            tops[value].append(key)

        max_count = len(nums) -k + 1
        result = []
        for count in range(max_count, 0, -1):
            for num in tops.get(count, []):
                result.append(num)
                if k == 1:
                    return result
                k -= 1
            
        return []
        