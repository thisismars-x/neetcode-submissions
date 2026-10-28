class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # cycle detection?
        # from collections import defaultdict
        # adj = defaultdict(list)
        adj = {k: [] for k in range(numCourses)}
        for a, b in prerequisites: adj[a].append(b)

        res = []

        visited, path = set(), set()
        def _dfs(node: int) -> bool:
            if node in path:
                return False # cycle
            if node in visited:
                return True # already processed

            path.add(node)
            for child in adj[node]:
                if not _dfs(child):
                    return False

            path.remove(node)
            visited.add(node)
            res.append(node)
            return True

        for i in range(numCourses):
            if i not in visited:
                if not _dfs(i):
                    return []

        return res

        
