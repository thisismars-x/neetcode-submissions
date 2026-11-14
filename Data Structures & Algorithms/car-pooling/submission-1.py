class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        import heapq

        trips.sort(key=lambda x: x[1])

        heap = []
        passengers = 0

        for n, start, end in trips:

            while heap and heap[0][0] <= start:
                end_time, count = heapq.heappop(heap)
                passengers -= count

            passengers += n

            if passengers > capacity:
                return False

            heapq.heappush(heap, (end, n))

        return True