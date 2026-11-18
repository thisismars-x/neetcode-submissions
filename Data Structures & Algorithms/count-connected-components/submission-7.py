class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        
        def _dfs(i: int):
            visited.add(i)
            
            for child in adj[i]:
                if child not in visited:
                    _dfs(child)
                    
        # count number of components
        nc = 0
        for i in range(n):
            if i not in visited:
                _dfs(i)
                nc += 1
        
        return nc