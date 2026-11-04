class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = [ [] for _ in range(n) ]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def _dfs(u: int):
            if u in visited:
                return
            visited.add(u)

            for child in adj[u]:
                _dfs(child)

        
        tc = 0
        for i in range(n):
            if i not in visited:
                tc += 1
                _dfs(i)

        return tc