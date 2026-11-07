class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x:x[1])
        tc = 0
        prev = -float('inf')

        for start, end in intervals:
            if start < prev:
                tc += 1
            else:
                prev = end

        return tc