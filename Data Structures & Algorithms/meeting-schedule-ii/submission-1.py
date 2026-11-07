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

        intervals.sort(key = lambda x: x.start)
        import heapq
        heap = []

        for inter in intervals:
            if heap and heap[0] <= inter.start:
                heapq.heappop(heap)
            heapq.heappush(heap, inter.end)

        return len(heap)
