class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        index = 0
        result = []
        while index < len(intervals):
            start, end = intervals[index]
            while index < (len(intervals) - 1) and end >= intervals[index + 1][0]:
                index += 1
                curr_interval = intervals[index] 
                end = max(end, curr_interval[1])
            result.append([start, end])
            index += 1

        return result