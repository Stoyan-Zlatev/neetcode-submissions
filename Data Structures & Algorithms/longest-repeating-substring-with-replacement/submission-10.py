class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #XYYXY
        l = 0
        n = len(s)
        max_length = 0
        while l < n:
            symbol = s[l]
            index = l + 1
            k_copy = k
            while index < n and (s[index] == symbol or k_copy > 0):
                if not s[index] == symbol:
                    k_copy -= 1
                index += 1

            curr_length = index -l + k_copy
            max_length=max(max_length, curr_length)

            while l < n and s[l] == symbol:
                l += 1

        return min(max_length, n)

            