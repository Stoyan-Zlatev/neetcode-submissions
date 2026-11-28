class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = l + (r - l) // 2
            if self.calculateTotal(piles, mid, h) > 0 :
                l = mid + 1
            else:
                r = mid - 1
                res = mid

        return res
            

    def calculateTotal(self, piles: List[int], rate: int, h: int) -> int:
        total_hours = 0
        for pile in piles:
            total_hours += math.ceil(pile/rate)

        return total_hours - h