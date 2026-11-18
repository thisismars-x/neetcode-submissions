class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        r, c = len(heights), len(heights[0])
        
        def _dfs(i, j, visited):
            stack = [(i, j)]
            visited.add((i, j))

            while stack:
                i2, j2 = stack.pop()
                for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    i3, j3 = i2 + di, j2 + dj
                    if 0 <= i3 < r and 0 <= j3 < c and heights[i3][j3] >= heights[i2][j2] and (i3, j3) not in visited:
                        stack.append((i3, j3))
                        visited.add((i3, j3))

        pac, atl = set(), set()
        for i in range(r):
            _dfs(i, c - 1, atl)
            _dfs(i, 0, pac)

        for i in range(c):
            _dfs(r - 1, i, atl)
            _dfs(0, i, pac)

        return list(atl & pac)

        
