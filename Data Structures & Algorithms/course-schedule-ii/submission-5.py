class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # this is like finding the valid topological ordering
        table = [ [] for _ in range(numCourses) ]
        indegree = [ 0 ] * numCourses
        
        for v, u in prerequisites:
            table[u].append(v)
            indegree[v] += 1
        
        res = []
        from collections import deque
        d = deque(x for x in range(numCourses) if indegree[x] == 0)
        
        while d:
            node = d.popleft()
            res.append(node)
            
            for children in table[node]:
                indegree[children] -= 1
                if indegree[children] == 0:
                    d.append(children)
                    
        return res if len(res) == numCourses else []
        