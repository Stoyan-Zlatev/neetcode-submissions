class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        tops = defaultdict(list)
        for key, value in counter.items():
            tops[value].append(key)

        curr = len(nums) -k + 1
        result = []
        while k > 0:
            if curr in tops:
                for num in tops[curr]:
                    result.append(num)
                    k -= 1
            curr -= 1

        return result
        