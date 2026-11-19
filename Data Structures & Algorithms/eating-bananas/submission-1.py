class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        stack = []
        while l <= r:
            mid = l - (l - r) // 2
            if self.calculateTotal(piles, mid, h) > 0 :
                l = mid + 1
            else:
                r = mid - 1
                stack.append(mid)

        return stack[-1]
            

    def calculateTotal(self, piles: List[int], rate: int, h: int) -> int:
        total_hours = 0
        for pile in piles:
            total_hours += math.ceil(pile/rate)

        return total_hours - h