class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        heap = list(Counter(tasks).values())
        import heapq
        heapq.heapify_max(heap)

        t = 0
        while heap:
            tmp = []

            for _ in range(n + 1):
                if heap:
                    f = heapq.heappop_max(heap) - 1
                    if f > 0:
                        tmp.append(f)

                t += 1
                if not heap and not tmp:
                    break

            for f in tmp:
                heapq.heappush_max(heap, f)


        return t