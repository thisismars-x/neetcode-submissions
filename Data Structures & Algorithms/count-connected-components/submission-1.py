class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()

        # convert edge list to adjacency list
        from collections import defaultdict
        d = defaultdict(list)

        for a, b in edges:
            d[a].append(b)
            d[b].append(a)
        

        def _bfs(node: int):
            if node in visited: return
            visited.add(node)
            
            for children in d[node]:
                _bfs(children)

        cunt = 0
        for nodes in range(n):
            if nodes not in visited:
                _bfs(nodes)
                cunt += 1

        return cunt