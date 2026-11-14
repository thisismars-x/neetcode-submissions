class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        import heapq
        heap = []

        heapq.heappush_max(heap, (a, 'a')) if a > 0 else None
        heapq.heappush_max(heap, (b, 'b')) if b > 0 else None
        heapq.heappush_max(heap, (c, 'c')) if c > 0 else None

        res = []

        while heap:
            freq, char = heapq.heappop_max(heap)
            if len(res) >= 2 and res[-1] == res[-2] == char:
                if not heap:
                    break

                freq2, char2 = heapq.heappop_max(heap)
                res.append(char2)
                heapq.heappush_max(heap, (freq2 - 1, char2)) if freq2 - 1 > 0 else None
                heapq.heappush_max(heap, (freq, char))

            else:
                res.append(char)
                heapq.heappush_max(heap, (freq - 1, char)) if freq - 1 > 0 else None

        return ''.join(res)