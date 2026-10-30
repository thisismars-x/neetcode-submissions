class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        r, c = len(board), len(board[0])

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def _dfs(i: int, j: int, k: int, used: set[tuple(int, int)]) -> bool:

            if len(word) == k + 1:
                return True

            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if 0 <= x < r and 0 <= y < c and board[x][y] == word[k + 1] and (x, y) not in used:
                    ## explore this direction
                    used.add((x, y))
                    if _dfs(x, y, k + 1, used):
                        return True
                    used.remove((x, y))

            return False

        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0]:
                    if _dfs(i, j, 0, {(i, j)}):
                        return True

        return False