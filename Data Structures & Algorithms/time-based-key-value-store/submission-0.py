class TimeMap:

    def __init__(self):
        from collections import defaultdict
        self._data = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        from bisect import insort
        insort(self._data[key], (timestamp, value) )
        

    def get(self, key: str, timestamp: int) -> str:
        n = len(self._data[key])

        lo, hi = 0, n - 1

        ans = ""
        while lo <= hi:
            mid = (lo + hi) // 2
            if self._data[key][mid][0] <= timestamp:
                ans = self._data[key][mid][1]
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
        
