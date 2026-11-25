class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        for index in range(len(intervals)):
            if not result or intervals[index][0] > result[-1][1]:
                result.append(intervals[index])
            else:
                result[-1][1] = max(intervals[index][1], result[-1][-1])

        return result