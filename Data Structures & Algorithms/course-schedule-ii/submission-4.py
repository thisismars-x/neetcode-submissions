class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for u, v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1
        

        # using kahns algorithm to gnereate some tpye of topological ordering?
        from collections import deque
        d = deque(i for i, x in enumerate(indegree) if x == 0)
        if len(d) == 0:
            # no topo sort is possible
            return []

        res = []
        while d:
            l = len(d)
            for _ in range(l):
                node = d.popleft()
                res.append(node)
                for child in adj[node]:
                    indegree[child] -= 1
                    if indegree[child] == 0:
                        d.append(child)

        
        return res if len(res) == numCourses else []