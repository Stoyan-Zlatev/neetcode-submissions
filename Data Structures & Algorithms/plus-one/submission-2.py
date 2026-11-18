class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        remember = 0
        if digits[-1] == 9:
            digits[-1] = 0
            remember = 1
        else:
            digits[-1] += 1
        for index in range(len(digits) - 2, -1, -1):
            if digits[index] == 9 and remember == 1:
                digits[index] = 0
                remember = 1
            else:
                digits[index] += remember
                remember = 0

        return [1] + digits if remember else digits
            