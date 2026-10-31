class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        r, c = len(matrix), len(matrix[0])
        
        # calculate the longest increasing path for each index
        #
        # LIP(i, j) = LIP(i - 1, j - 1) + ... + 1 if element at i, j is less

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        profits = {}

        def _dfs(i: int, j: int) -> int:
            
            if (i, j) in profits:
                return profits[(i, j)]

            cp = 1
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