class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # cycle detection
        adj = [ [] for _ in range(numCourses) ]
        indegree = [ 0 ] * numCourses
        for u, v in prerequisites:
            adj[u].append(v)
            indegree[v] += 1

        from collections import deque
        d = deque(i for i, n in enumerate(indegree) if n == 0)

        count = 0

        while d:
            node = d.popleft()
            count += 1

            for children in adj[node]:
                indegree[children] -= 1
                if indegree[children] == 0:
                    d.append(children)

        return count == numCourses


        


