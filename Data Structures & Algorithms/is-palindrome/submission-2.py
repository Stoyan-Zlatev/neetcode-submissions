class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ""
        for letter in s:
            if letter.isalnum():
                filtered+=letter.lower()
        s_length = len(filtered) // 2
        for i in range(s_length):
            if not filtered[i] == filtered[-i-1]:
                return False

        return True