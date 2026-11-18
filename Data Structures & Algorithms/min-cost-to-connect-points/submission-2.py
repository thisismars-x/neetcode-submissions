class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
       
       class DSU:
       
            def __init__(self, n: int):
                self.parents = list(range(n))
                self.rank = [1] * n
                self.nc = 0
                
            def find(self, a: int) -> int:
                while self.parents[a] != a:
                    self.parents[a] = self.parents[self.parents[a]]
                    a = self.parents[a]
                return a
                
            def union(self, a: int, b: int) -> bool:
                ra, rb = self.find(a), self.find(b)
                if ra == rb: return False
                
                if self.rank[ra] < self.rank[rb]: ra, rb = rb, ra
                self.parents[rb] = ra
                self.rank[ra] += self.rank[rb]
                self.nc += 1
                return True
                
       n = len(points)
       uf = DSU(n)
       
       edges = []
       for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                
                d = abs(x1 - x2) + abs(y1 - y2)
                edges.append((d, i, j))
    
       edges.sort()
       mst = 0
        
       for d, i, j in edges:
           if uf.nc == n:
               break
            
           if uf.union(i, j):
               mst += d
        
       return mst