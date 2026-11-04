class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        class DSU:
            def __init__(self, n: int):
                self.parents = list(range(n))
            def find(self, a: int) -> int:
                while a != self.parents[a]:
                    self.parents[a] = self.parents[self.parents[a]]
                    a = self.parents[a]
                return a

            def union(self, a: int, b: int) -> bool:
                ra, rb = self.find(a), self.find(b)
                if ra == rb:
                    return False

                self.parents[ra] = rb
                return True

        uf = DSU(len(edges))
        for u, v in edges:
            if not uf.union(u - 1, v - 1):
                return [u, v]

