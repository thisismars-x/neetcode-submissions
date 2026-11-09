class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        reach = [[False] * numCourses for _ in range(numCourses)]
        for u, v in prerequisites:
            reach[u][v] = True

        for i in range(numCourses):
            for j in range(numCourses):
                for k in range(numCourses):
                    reach[j][k] |= reach[j][i] and reach[i][k]

        return [reach[u][v] for u, v in queries]