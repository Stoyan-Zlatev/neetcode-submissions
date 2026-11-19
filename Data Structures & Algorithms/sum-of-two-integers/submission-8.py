class Solution:
    def getSum(self, a: int, b: int) -> int:
        curr_bit = 1
        carry = 0
        result = 0
        for i in range(32):
            left = 1 if (curr_bit & a) else 0
            right = 1 if (curr_bit & b) else 0
            sum_bits = left ^ right ^ carry
            if sum_bits:
                result ^= curr_bit
            carry = (left & right) | (carry & (left ^ right))
            curr_bit <<= 1

        if result > 0x7FFFFFFF:
            mask = 0xFFFFFFFF
            result = ~(result ^ mask)

        return result
