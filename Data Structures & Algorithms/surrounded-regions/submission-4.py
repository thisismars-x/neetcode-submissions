class Solution:
    def solve(self, board: List[List[str]]) -> None:
        r, c = len(board), len(board[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        visited = set()

        def _dfs(i: int, j: int, res: list[tuple[int, int]]):
            stack = [(i, j)]
            visited.add((i, j))

            while stack:
                i, j = stack.pop()
                res.append((i, j))

                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy

                    if (
                        0 <= ni < r
                        and 0 <= nj < c
                        and board[ni][nj] == 'O'
                        and (ni, nj) not in visited
                    ):
                        visited.add((ni, nj))
                        stack.append((ni, nj))

        res = []

        for i in range(r):
            for j in range(c):
                tmp = []

                if board[i][j] == 'O' and (i, j) not in visited:
                    _dfs(i, j, tmp)

                    # Region doesn't touch boundary
                    if all(
                        i != 0 and i != r - 1 and
                        j != 0 and j != c - 1
                        for i, j in tmp
                    ):
                        res.append(tmp)

        for region in res:
            for i, j in region:
                board[i][j] = 'X'