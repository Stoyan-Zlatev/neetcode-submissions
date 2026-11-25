"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        heap = [intervals[0].end]
        result = 1
        index = 0
        for index in range(1, len(intervals)):
            start, end = intervals[index].start, intervals[index].end
            if heap and heap[0] <= start:
                heapq.heappop(heap)
            else:
                result += 1
            
            heapq.heappush(heap, end)


        return result 
        