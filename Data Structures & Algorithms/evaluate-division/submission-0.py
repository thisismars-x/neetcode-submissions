class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        from collections import defaultdict
        adj = defaultdict(list)

        for eq, w in zip(equations, values):
            u, v = eq
            adj[u].append((v, w))
            adj[v].append((u, 1 / w))
        

        def _bfs(src: str, target: str) -> float:
            if src not in adj or target not in adj:
                return -1.0


            from collections import deque
            visited = set()
            d = deque([(src,1)]) # you get v, and w

            visited.add(src)

            while d:
                v, w = d.popleft()

                if v == target:
                    return w

                for children, cw in adj[v]:
                    if children not in visited:
                        visited.add(children)
                        d.append((children, w * cw))

            return -1.0

        return [ _bfs(*q) for q in queries ]



