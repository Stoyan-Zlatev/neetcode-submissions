class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        # [[1,2],[3,4]]
        # [2,3]
        # do not forget if newInterval[1] < intervals[0][0]
        result = []
        index = 0
        while index < len(intervals):
            curr_start, curr_end = intervals[index]
            if newInterval[1] < curr_start:
                result.append(newInterval)
                result.append(intervals[index])
                index += 1
                break
            elif newInterval[0] <= curr_end:
                curr_start = min(newInterval[0], curr_start)
                curr_end = max(intervals[index][1], newInterval[1])
                while index < len(intervals) and intervals[index][0] <= newInterval[1]:
                    curr_end = max(intervals[index][1], curr_end)
                    index += 1
                result.append([curr_start, curr_end])
                break
            index += 1
            result.append([curr_start, curr_end])

        for i in range(index, len(intervals)):
            result.append(intervals[i])

        if newInterval[0] > result[-1][1]:
            result.append(newInterval)

        return result