        
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        adj = [ [] for _ in range(n) ]        
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def _dfs(node: int, parent: int) -> int:
            h = 0
            for children in adj[node]:
                if children != parent:
                    h = max(h, 1 + _dfs(children, node))
            return h

        mh = n
        res = []

        for i in range(n):
            h = _dfs(i, -1)
            if h == mh:
                res.append(i)
            elif h < mh:
                mh = h
                res = [i]

        return res

            
