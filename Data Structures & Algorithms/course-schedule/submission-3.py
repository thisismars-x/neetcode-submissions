class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[v].append(u)

        visited = [0] * numCourses

        def _dfs(u: int) -> bool:
            if visited[u] == 1:
                return False
            if visited[u] == 2:
                return True

            visited[u] = 1
            for child in adj[u]:
                if not _dfs(child):
                    return False

            visited[u] = 2
            return True

        for i in range(numCourses):
            if not _dfs(i):
                return False

        return True

            