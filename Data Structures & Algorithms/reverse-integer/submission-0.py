class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        MAX, MIN = 2**31 - 1, -2**31
        is_negative = x < 0
        x = abs(x)
        while x:
            digit = x % 10
            x //= 10
            if (MIN // 10 < res < MAX//10) or (MAX//10 == res and digit < MAX % 10) or (MIN//10 == res and digit < (MIN % 10)):
                res *= 10
                res += digit
            else:
                return 0

        return -res if is_negative else res
