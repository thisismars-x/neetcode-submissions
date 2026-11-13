class Solution:
    def reorganizeString(self, s: str) -> str:

        from collections import Counter
        from heapq import heapify, heappop, heappush

        heap = [(-freq, char) for char, freq in Counter(s).items()]
        heapify(heap)

        res = []
        prev = None

        while heap:
            freq, char = heappop(heap)

            res.append(char)
            freq += 1  # negative frequency: increment toward zero

            if prev:
                heappush(heap, prev)

            prev = (freq, char) if freq < 0 else None

        return ''.join(res) if len(res) == len(s) else ''