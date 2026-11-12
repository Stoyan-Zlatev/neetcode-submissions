class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ""
        for symbol in s:
            if symbol.isalnum():
                filtered += symbol.lower()

        return filtered == filtered[::-1]