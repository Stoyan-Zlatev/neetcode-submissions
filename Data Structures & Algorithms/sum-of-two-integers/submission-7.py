class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 30 = 16 + 8 + 4 + 2
        # 10100
        # 11110
        #      110010 = 32 + 16 + 2 = 50
        # 0 - 0
        # 10 - 2
        # 010 - 2
        # 0010 - 2
        # 10010 - 18
        # 110010 - 50
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
