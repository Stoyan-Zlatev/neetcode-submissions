class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #XYYXY
        counter = defaultdict(int)
        n = len(s)
        max_length = 0
        most_freq = 0
        l = 0
        for r in range(n):
            counter[s[r]] += 1
            most_freq = max(most_freq, counter[s[r]])
            if (r -l + 1) - most_freq > k:
                counter[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)

        return max_length
        

            