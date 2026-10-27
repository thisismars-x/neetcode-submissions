class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # is this a find if there is a loop in the graph question?
        # prereq is kind of like an edge list?

        from collections import defaultdict
        table = defaultdict(list)
        for a, b in prerequisites: table[b].append(a)

        visited = set()
        path = set()

        def _dfs(node: int):
            if node in path: return False
            if node in visited: return True
            path.add(node)

            visited.add(node)

            for children in table[node]:
                if not _dfs(children):
                    return False

            path.remove(node)
            visited.add(node)
            return True

        for i in range(numCourses):
            if i not in visited:
                if not _dfs(i):
                    return False

        return True 