class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_length = len(s)
        # YXAZXY, XYZ
        if s_length < len(t):
            return ""
        
        letters = Counter(t)

        l, r = 0, 0
        min_substr = s + 'a'
        curr_window = defaultdict(int)
        required = len(letters)
        formed = 0
        for r in range(s_length):
            curr_window[s[r]] += 1
            if s[r] in letters and curr_window[s[r]]  == letters[s[r]]:
                    formed += 1
                
            while l <= r and formed == required:
                if (r-l+1) < len(min_substr):
                    min_substr = s[l:r+1] 
                    
                if s[l] in letters and curr_window[s[l]] == letters[s[l]]:
                    formed -= 1
                curr_window[s[l]] -= 1
                l += 1

        return min_substr if len(min_substr) <= len(s) else ""
                    

