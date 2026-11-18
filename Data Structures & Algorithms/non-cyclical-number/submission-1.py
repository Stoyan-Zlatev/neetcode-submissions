class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while not n in seen:
            seen.add(n)
            curr_sum = 0
            while n:
                curr_sum += pow(n%10,2)
                n //= 10

            if curr_sum == 1:
                return True

            n = curr_sum

        return False
      