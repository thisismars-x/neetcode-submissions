class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        
        class DSU:
            def __init__(self, n: int):
                self.parents = list(range(n))
                self.ncomponents = n

            def find(self, a: int) -> int:
                while self.parents[a] != a:
                    self.parents[a] = self.parents[self.parents[a]]
                    a = self.parents[a]
                return a

            def union(self, a: int, b: int) -> bool:
                ra, rb = self.find(a), self.find(b)
                if ra == rb:
                    return False

                self.parents[ra] = rb
                self.ncomponents -= 1

        uf = DSU(n)
        for u, v in edges:
            uf.union(u, v)

        return uf.ncomponents