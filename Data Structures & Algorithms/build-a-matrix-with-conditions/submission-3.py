class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:


        def _topo(el: list[list[int]]) -> list[int]:
            from collections import defaultdict, deque

            adj = defaultdict(list)
            indegree = [ 0 ] * k
            for u, v in el:
                adj[u].append(v)
                indegree[v - 1] += 1

            d = deque(x + 1 for x in range(k) if indegree[x] == 0)
            order = []

            while d:
                node = d.popleft()
                order.append(node)

                for children in adj[node]:
                    indegree[children - 1] -= 1
                    if indegree[children - 1] == 0:
                        d.append(children)

            return order if len(order) == k else []

        row, col = _topo(rowConditions), _topo(colConditions)
        if not (row and col):
            return []

        row = {n: i for i, n in enumerate(row)}
        col = {n: i for i, n in enumerate(col)}

        res = [ [ 0 ] * k for _ in range(k) ]
        for i in range(1, k + 1):
            res[row[i]][col[i]] = i

        return res