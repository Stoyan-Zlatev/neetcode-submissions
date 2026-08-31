class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        letters = {}
        for letter in s:
            letters[letter] = letters.get(letter,0) + 1
        for letter in t:
            if letters.get(letter,0) == 0:
                return False
            letters[letter] -= 1
        return True
