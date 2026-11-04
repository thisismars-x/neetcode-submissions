class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        # this is dsu solvable
        class DSU:
            def __init__(self, n: int):
                self.parents = list(range(n))
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
                return True

        
            
        uf = DSU(n)
        for u,v in edges:
            if not uf.union(u, v):
                return False
        return True

        