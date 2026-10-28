class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # cycle detection?
        from collections import defaultdict
        adj = defaultdict(list)
        for a, b in edges: 
            adj[a].append(b)
            adj[b].append(a)

        visited = set()

        def _dfs(node: int, parent: int) -> bool:
            if node in visited: return False
            visited.add(node)

            for children in adj[node]:
                if children == parent:
                    continue
                if not _dfs(children, node):
                    return False

            return True

        # one dfs should make it a tree(otherwise unconnected components)
        return _dfs(0, -1) and len(visited) == n