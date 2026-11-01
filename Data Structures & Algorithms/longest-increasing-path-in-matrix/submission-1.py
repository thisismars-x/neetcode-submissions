class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:


        r, c = len(matrix), len(matrix[0])
        d = [ [0] * c for _ in range(r) ]

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        from functools import cache
        @cache
        def _dfs(i: int, j: int):
            if not (0 <= i < r or 0 <= j < c):
                return 0


            tl = 1
            for di, dj in dirs:
                _i, _j = i + di, j + dj
                if 0 <= _i < r and 0 <= _j < c and matrix[_i][_j] > matrix[i][j]:
                    tl = max(tl, 1 + _dfs(_i, _j))

            return tl

        tl = 1
        for i in range(r):
            for j in range(c):
                tl = max(tl, _dfs(i, j))

        return tl














        r, c = len(matrix), len(matrix[0])
        
        # calculate the longest increasing path for each index
        #
        # LIP(i, j) = LIP(i - 1, j - 1) + ... + 1 if element at i, j is less

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        profits = {}

        def _dfs(i: int, j: int) -> int:
            
            if (i, j) in profits:
                return profits[(i, j)]

            cp = 1 # shortest path is always at least len == 1
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < r and 0 <= nj < c and matrix[ni][nj] > matrix[i][j]:
                    cp = max(cp, 1 + _dfs(ni, nj))

            profits[(i, j)] = cp
            return cp

        ans = 0
        for i in range(r):
            for j in range(c):
                ans = max(_dfs(i, j), ans)

        return ans