"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key = lambda x: x.start)

        end = intervals[0].end
        for inter in intervals[1:]:
            s, e = inter.start, inter.end
            if s < end:
                return False
            end = e

        return True
