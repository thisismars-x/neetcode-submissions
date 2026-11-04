class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        r, c = len(board), len(board[0])

        visited = set()

        def _dfs(i: int, j: int, tmp: list[tuple[int, int]]):
            stack = [(i, j)]

            while stack:
                i, j = stack.pop()

                if (i, j) in visited:
                    continue

                visited.add((i, j))
                tmp.append((i, j))

                for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    i2, j2 = i + di, j + dj

                    if (
                        0 <= i2 < r and
                        0 <= j2 < c and
                        board[i2][j2] == 'O' and
                        (i2, j2) not in visited
                    ):
                        stack.append((i2, j2))

        res = []
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O' and (i, j) not in visited:
                    tmp = []
                    _dfs(i, j, tmp)

                    if all(
                        _i != 0 and _i != r - 1 and
                        _j != 0 and _j != c - 1
                        for _i, _j in tmp
                    ):
                        res.extend(tmp)

        for i, j in res:
            board[i][j] = 'X'