class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        
        adj = [[] for _ in range(n + 1)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = [False] * (n + 1)
        cycle, start = set(), -1

        def _dfs(node: int, p: int) -> bool:
            nonlocal start
            if visited[node]:
                start = node
                return True

            visited[node] = True
            for n in adj[node]:
                if n == p: continue

                if _dfs(n, node):
                    if start != -1:
                        cycle.add(node)
                    if node == start:
                        start = -1 # full cicrcle
                    return True

            return False

        _ = _dfs(1, -1)

        for a, b in edges[::-1]: # from last
            if a in cycle and b in cycle:
                return [a, b]

        return []
