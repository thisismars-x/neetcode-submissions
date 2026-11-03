class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        import heapq
        from math import sqrt
        points = [
            (
                sqrt( (x1 - 0) ** 2 + (x2 - 0) ** 2 ),
                (x1, x2)
            )
            for (x1, x2) in points
        ]

        heapq.heapify(points)
        res = []
        for _ in range(k):
            _ds, point = heapq.heappop(points)
            res.append(list(point))

        return res