class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        max_length = 0
        seen = {}
        for end in range(len(s)):
            if seen.get(s[end],0) == 0:
                seen[s[end]] = 1
                max_length = max(max_length, end - start + 1)
            else:
                while not s[start] == s[end]:
                    seen[s[start]] = 0
                    start += 1
                start += 1

        return max_length