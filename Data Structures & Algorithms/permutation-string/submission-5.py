class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length = len(s1)
        if s1_length > len(s2):
            return False

        counter = Counter(s1)
        curr_counter = Counter(s2[:s1_length])
        if curr_counter == counter:
            return True
        for i in range(s1_length, len(s2)):
            curr_counter[s2[i-s1_length]]-=1
            curr_counter[s2[i]] += 1
            if curr_counter == counter:
                return True
        return False