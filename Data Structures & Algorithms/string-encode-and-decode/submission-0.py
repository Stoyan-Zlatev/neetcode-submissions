class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += f"{len(word)}#{word}"
        return result
    def decode(self, s: str) -> List[str]:
        result = []
        s_length = len(s)
        iterator = 0
        while iterator < s_length:
            w_length = ""
            while not s[iterator] ==  '#':
                w_length += s[iterator]
                iterator += 1
            iterator+=1
            w_length = int(w_length)
            d_word = s[iterator:(iterator+w_length)]
            iterator += w_length
            result.append(d_word)

        return result