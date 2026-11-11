class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r, c = len(heights), len(heights[0])
        
        def _dfs(i: int, j: int, v: set[int], prev: int):
            if (
                not (0 <= i < r and 0 <= j < c) or
                (i, j) in v or
                prev > heights[i][j]
            ):
                return

            v.add((i, j))

            _dfs(i + 1, j, v, heights[i][j])
            _dfs(i - 1, j, v, heights[i][j])
            _dfs(i, j + 1, v, heights[i][j])
            _dfs(i, j - 1, v, heights[i][j])


        pac, atl = set(), set()

        for i in range(r):
            _dfs(i, c - 1, atl, -1)
            _dfs(i, 0, pac, -1)

        for i in range(c):
            _dfs(r - 1, i, atl, -1)
            _dfs(0, i, pac, -1)

        res = []
        for i in range(r):
            for j in range(c):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])

        return res