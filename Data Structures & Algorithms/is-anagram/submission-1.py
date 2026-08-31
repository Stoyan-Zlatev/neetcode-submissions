class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        letters = [0] * 26
        len_s = len(s)
        for i in range(len_s):
            letters[ord(s[i])-ord('a')]+=1
            letters[ord(t[i])-ord('a')]-=1

        for i in range(26):
            if letters[i] > 0:
                return False
        return True
