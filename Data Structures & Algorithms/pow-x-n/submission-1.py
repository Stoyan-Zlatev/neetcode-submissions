class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 0
        if n == 0:
            return 1
        if n == 1:
            return x
        if n % 2 == 1:
            result = x * self.myPow(x*x, abs(n)//2)
        else:
            result = self.myPow(x*x, abs(n)//2)

        return result if n > 0 else 1 / result