class Solution:
    def minEatingSpeed(self, apples: List[int], h: int) -> int:
        l, r = 1, max(apples)
        min_rate = r
        while l <= r:
            mid = l + (r - l) // 2
            diff = self.canEatBananas(apples, mid, h)
            if diff >= 0:
                min_rate = mid
                r = mid - 1
            else:
                l = mid + 1

        return min_rate

        
    def canEatBananas(self, apples: List[int], rate: int, target: int) -> int:
        total_hours = 0
        for apple_count in apples:
            total_hours += math.ceil(apple_count / rate)

        return target - total_hours