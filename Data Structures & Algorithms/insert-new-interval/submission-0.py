class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        from bisect import bisect_left

        pos = bisect_left(intervals, newInterval)

        tmp = pos
        while tmp > 0 and intervals[tmp - 1][1] >= newInterval[0]:
            newInterval[0] = min(newInterval[0], intervals[tmp - 1][0])
            newInterval[1] = max(newInterval[1], intervals[tmp - 1][1])
            tmp -= 1

        tmp2 = pos
        while tmp2 < len(intervals) and intervals[tmp2][0] <= newInterval[1]:
            newInterval[1] = max(newInterval[1], intervals[tmp2][1])
            tmp2 += 1

        return intervals[:tmp] + [newInterval] + intervals[tmp2:]