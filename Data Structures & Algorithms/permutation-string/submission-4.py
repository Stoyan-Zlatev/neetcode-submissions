class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length = len(s1)
        if s1_length > len(s2):
            return False

        counter = Counter(s1)
        index = 0
        while index < len(s2) - len(s1) + 1:
            if s2[index] in counter:
                temp_counter = defaultdict(int)
                for i in range(index, index + s1_length):
                    if not s2[i] in counter:
                        break
                    temp_counter[s2[i]] += 1
                if temp_counter == counter:
                    return True
            index += 1
        return False