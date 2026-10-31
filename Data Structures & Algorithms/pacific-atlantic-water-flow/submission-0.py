class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r, c, p, a = len(heights), len(heights[0]), set(), set()

        def _dfs(i: int, j: int, visited: set, prev: int):
            if ( not (0 <= i < r and 0 <= j < c) ) or ( (i, j) in visited ) or heights[i][j] < prev:
                return

            visited.add((i, j))
            _dfs(i + 1, j, visited, heights[i][j])
            _dfs(i - 1, j, visited, heights[i][j])
            _dfs(i, j + 1, visited, heights[i][j])
            _dfs(i, j - 1, visited, heights[i][j])


        for i in range(c):
            _dfs(0, i, p, heights[0][i])
            _dfs(r - 1, i, a, heights[r-1][i])

        for i in range(r):
            _dfs(i, 0, p, heights[i][0])
            _dfs(i, c - 1, a, heights[i][c-1])

        res = []
        for i in range(r):
            for j in range(c):
                if (i, j) in p and (i, j) in a:
                    res.append([i, j])

        return res

        