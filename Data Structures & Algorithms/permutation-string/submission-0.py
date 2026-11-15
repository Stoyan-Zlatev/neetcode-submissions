class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        s1_length = len(s1)
        for index, letter in enumerate(s2):
            if letter in counter:
                if Counter(s2[index:index+s1_length]) == counter:
                    return True

        return False