class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        pending, avail = [], []

        import heapq

        for idx, (et, pt) in enumerate(tasks):
            heapq.heappush(pending, (et, pt, idx))

        ctime, res = 0, []
        while pending or avail:
            while pending and pending[0][0] <= ctime:
                et, pt, i = heapq.heappop(pending)
                heapq.heappush(avail, (pt, i))

            if not avail:
                ctime = pending[0][0]
                continue

            pt, i = heapq.heappop(avail)
            ctime += pt
            res.append(i)

        return res
