class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [ ['.'] * n for _ in range(n) ]

        def _valid(i: int, j: int) -> bool:
            # # queen can attack horizontally
            for k in range(j):
                if board[i][k] == 'Q':
                    return False

            for k in range(i):
                if board[k][j] == 'Q':
                    return False

            # diagonally
            i1, j1 = i - 1, j - 1
            while i1 >= 0 and j1 >= 0:
                if board[i1][j1] == 'Q':
                    return False
                i1 -= 1
                j1 -= 1
            i1, j1 = i - 1, j + 1
            while i1 >= 0 and j1 < n:
                if board[i1][j1] == 'Q':
                    return False
                i1 -= 1
                j1 += 1
            return True

        res = []

        def _dfs(r: int):
            if r == n:
                res.append(list("".join(x) for x in board))
                return

            for c in range(n):
                if not _valid(r, c):
                    continue

                board[r][c] = 'Q'
                _dfs(r + 1)
                board[r][c] = '.'

        _dfs(0)

        return res























        