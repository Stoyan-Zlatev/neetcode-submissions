class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = defaultdict(list)
        print(result[0])
        counter = defaultdict(int)
        for num in nums:
            counter[num] =counter.get(num,0) + 1

        for key, value in counter.items():
            result[value].append(key)

        new_res=[]
        for i in range(len(nums),-1,-1):
            for el in result[i]:
                new_res.append(el)
                k-=1
            if k==0:break

        return new_res