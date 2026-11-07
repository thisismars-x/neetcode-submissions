class CountSquares:

    def __init__(self):
        from collections import defaultdict
        self.pt, self.ptc = [], defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.pt.append(point)
        self.ptc[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0

        for x, y in self.pt:
            if (
                abs(point[0] - x) != abs(point[1] - y) or 
                x == point[0] or y == point[1]
            ):
                continue

            res += self.ptc[(x, point[1])] * self.ptc[(point[0], y)]

        return res

