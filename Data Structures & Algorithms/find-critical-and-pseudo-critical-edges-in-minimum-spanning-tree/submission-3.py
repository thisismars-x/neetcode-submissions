class DSU:
    def __init__(self, n: int):
        self.par = list(range(n))
        self.components = n

    def find(self, a: int) -> int:
        if self.par[a] != a:
            self.par[a] = self.find(self.par[a])
        return self.par[a]

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        self.par[rb] = ra
        self.components -= 1
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        new_edges = [[u, v, w, i] for i, (u, v, w) in enumerate(edges)]
        new_edges.sort(key=lambda x: x[2])

        base_mst = 0
        uf = DSU(n)
        for u, v, w, _ in new_edges:
            if uf.union(u, v):
                base_mst += w

        critical = []
        pseudo_critical = []

        for u, v, w, i in new_edges:
            c_uf = DSU(n)
            c_mst = 0
            for u2, v2, w2, i2 in new_edges:
                if i2 != i and c_uf.union(u2, v2):
                    c_mst += w2

            if c_uf.components > 1 or c_mst > base_mst:
                critical.append(i)
                continue

            p_uf = DSU(n)
            p_uf.union(u, v)
            p_mst = w
            for u2, v2, w2, i2 in new_edges:
                if p_uf.union(u2, v2):
                    p_mst += w2

            if p_mst == base_mst:
                pseudo_critical.append(i)

        return [critical, pseudo_critical]