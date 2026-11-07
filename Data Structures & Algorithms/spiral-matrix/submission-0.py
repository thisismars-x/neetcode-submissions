class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r, c = len(matrix), len(matrix[0])

        spiral_directions = {
            'r': [0, +1],
            'l': [0, -1],
            'd': [+1, 0],
            'u': [-1, 0]
        }

        spiral_next_directions = {
            'r': 'd',
            'd': 'l',
            'l': 'u',
            'u': 'r'
        }

        visited = set()
        res = []

        def _dfs(i: int, j: int, direction: str):
            if not (0 <= i < r and 0 <= j < c) or (i, j) in visited:
                return 

            visited.add((i, j))
            res.append(matrix[i][j])

            di, dj = spiral_directions[direction]
            i2, j2 = i + di, j + dj

            if 0 <= i2 < r and 0 <= j2 < c and (i2, j2) not in visited:
                _dfs(i2, j2, direction)

            next_direction = spiral_next_directions[direction]
            di, dj = spiral_directions[next_direction]
            _dfs(i + di, j + dj, next_direction)

        _dfs(0, 0, 'r')
        return res