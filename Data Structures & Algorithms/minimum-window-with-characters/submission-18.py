class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_length = len(s)
        # YXAZXY, XYZ
        if s_length < len(t):
            return ""
        
        letters = Counter(t)

        l, r = 0, 0
        res = []
        min_len = float('inf')
        curr_window = defaultdict(int)
        required = len(letters)
        formed = 0
        for r in range(s_length):
            curr_window[s[r]] += 1
            if s[r] in letters and curr_window[s[r]]  == letters[s[r]]:
                    formed += 1
                
            while l <= r and formed == required:
                if (r-l+1) < min_len:
                    res = [l,r+1]
                    min_len = (r-l+1) 

                if s[l] in letters and curr_window[s[l]] == letters[s[l]]:
                    formed -= 1
                curr_window[s[l]] -= 1
                l += 1

        return s[res[0]:res[1]] if not min_len == float('inf') else ""
                    

