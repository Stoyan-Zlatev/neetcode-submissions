class Solution:
    def hammingWeight(self, n: int) -> int:
        # 23 / 2
        # 11 1 = 16
        # 5 1 = 8
        # 2 1 = 4
        # 1 0 = 
        # 0 1 =
        result = 0
        while n:
            result += n % 2
            n //= 2

        return result