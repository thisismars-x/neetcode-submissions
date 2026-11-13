class Solution:
    def totalNQueens(self, n: int) -> int:

        board = [ [ '.' ] * n for _ in range(n) ]
        
        def _valid(i: int, j: int) -> bool:

            # check vertical
            for k in range(i):
                if board[k][j] == 'Q':
                    return False

            # check diagonal
            k, l = i - 1, j - 1
            while k >= 0 and l >= 0:
                if board[k][l] == 'Q':
                    return False

                k -= 1
                l -= 1

            k, l = i - 1, j + 1
            while k >= 0 and l < n:
                if board[k][l] == 'Q':
                    return False

                k -= 1
                l += 1

            return True

        
        res = 0

        def _dfs(row: int):
            nonlocal res

            if row == n:
                res += 1
                return

            for col in range(n):
                if _valid(row, col):
                    board[row][col] = 'Q'
                    _dfs(row + 1)
                    board[row][col] = '.'

        _dfs(0)
        return res








