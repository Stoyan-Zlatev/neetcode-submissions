class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = len(nums)
        result = [[] for i in range(num_count+1)]
        counter = {}
        for num in nums:
            counter[num] =counter.get(num,0) + 1

        for key, value in counter.items():
            result[value].append(key)

        new_res=[]
        for i in range(num_count,0,-1):
            for el in result[i]:
                new_res.append(el)
                if k==1:return new_res
                k-=1

        return []