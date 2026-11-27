class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        seen = set()
        l = 0 
        longest = 0

        for index in range(n):
            while s[index] in seen:
                seen.remove(s[l])
                l += 1
                
            curr_length = index - l + 1
            longest = max(longest, curr_length)
            seen.add(s[index])

        return longest