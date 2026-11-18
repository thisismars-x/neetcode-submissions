class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        from collections import defaultdict
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = set()
        
        def _dfs(i: int, parent: int) -> bool:
            if i in visited:
               return False

            visited.add(i)
            
            for child in adj[i]:
                if child == parent:
                    continue
                
                if child in visited:
                    return False
                    
                if not _dfs(child, i):
                    return False
            
            return True

        return _dfs(0, -1) and len(visited) == n