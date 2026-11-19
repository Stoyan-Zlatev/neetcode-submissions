class Solution:
    def countBits(self, n: int) -> List[int]:
        save = {0: 0, 1: 1}
        result = [0] * (n + 1)
        for i in range(1, n+1):
            counter = 0
            curr_num = i
            while not curr_num in save:
                counter += 1
                curr_num &= (curr_num - 1)

            counter += save[curr_num]
            save[i] = counter
            result[i] = counter

        return result