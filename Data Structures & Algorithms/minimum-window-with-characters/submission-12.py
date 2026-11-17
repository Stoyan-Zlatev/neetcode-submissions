class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_length = len(s)
        # YXAZXY, XYZ
        if s_length < len(t):
            return ""
        
        letters = {}
        for letter in t:
            letters[letter] = letters.get(letter, 0) + 1

        l, r = 0, 0
        min_substr = s + 'a'
        curr_window = defaultdict(int)
        required = len(letters)
        formed = 0
        while r < s_length:
            if not formed == required:
                curr_window[s[r]] += 1
                if s[r] in letters and curr_window[s[r]]  == letters[s[r]]:
                    formed += 1
                r += 1
            else:
                while l <= r and formed == required:
                    min_substr = s[l:r] if (r-l) < len(min_substr) else min_substr
                    if s[l] in letters and curr_window[s[l]] == letters[s[l]]:
                        formed -= 1
                    curr_window[s[l]] -= 1
                    l += 1

        if r == s_length and formed:
            while l <= r and formed == required:
                min_substr = s[l:r] if (r-l) < len(min_substr) else min_substr
                if s[l] in letters and curr_window[s[l]] == letters[s[l]]:
                    formed -= 1
                curr_window[s[l]] -= 1
                l += 1

        return min_substr if len(min_substr) <= len(s) else ""
                    

