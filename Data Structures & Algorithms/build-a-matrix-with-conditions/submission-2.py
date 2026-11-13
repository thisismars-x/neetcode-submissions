class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def _dfs(s: int, adj: dict[int, list[int]], visit: set[int], path: set[int], order: list[int]) -> bool:

            if s in path:
                return False

            if s in visit:
                return True

            path.add(s)
            visit.add(s)

            for children in adj[s]:
                if not _dfs(children, adj, visit, path, order):
                    return False

            path.remove(s)
            order.append(s)
            return True

        def _topo(el: list[[list[int]]]) -> list[int]:
            adj = defaultdict(list)
            for u, v in el:
                adj[u].append(v)

            visit, path = set(), set()
            order = []
            for s in range(1, 1 + k):
                if s not in visit:
                    if not _dfs(s, adj, visit, path, order):
                        return []

            return order[::-1]
                
        row = _topo(rowConditions)
        if not row:
            return []

        col = _topo(colConditions)
        if not col:
            return []

        val_row, val_col = {n: i for i, n in enumerate(row)}, {n: i for i, n in enumerate(col)}
        res = [ [ 0 ] * k for _ in range(k) ]
        for n in range(1, 1 + k):
            r, c = val_row[n], val_col[n]
            res[r][c] = n

        return res
