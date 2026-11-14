class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        meetings.sort()

        avail = list(range(n))
        used = []

        count = [ 0 ] * n

        for s, e in meetings:
            while used and used[0][0] <= s:
                e2, room = heapq.heappop(used)
                heapq.heappush(avail, room)

            if not avail:
                e2, room = heapq.heappop(used)
                e = e2 + (e - s)
                heapq.heappush(avail, room)

            room = heapq.heappop(avail)
            heapq.heappush(used, (e, room))
            count[room] += 1

        return count.index(max(count))
