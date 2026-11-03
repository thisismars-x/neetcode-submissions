class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        from bisect import insort
        insort(self.data, num)

    def findMedian(self) -> float:
        n = len(self.data)
        mid = n // 2

        if n & 1:
            return float(self.data[mid])

        return (self.data[mid - 1] + self.data[mid]) / 2