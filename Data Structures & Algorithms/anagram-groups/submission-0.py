class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            l_counter = [0] * 26
            for letter in word:
                l_counter[ord(letter)-ord('a')] += 1
            result[tuple(l_counter)].append(word)

        return list(result.values())
   
        