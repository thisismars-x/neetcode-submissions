class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r, c = len(matrix), len(matrix[0])

        self.pmatrix = [[0] * (c + 1) for _ in range(r + 1)]

        for i in range(1, r + 1):
            for j in range(1, c + 1):
                self.pmatrix[i][j] = (
                    matrix[i - 1][j - 1]
                    + self.pmatrix[i - 1][j]
                    + self.pmatrix[i][j - 1]
                    - self.pmatrix[i - 1][j - 1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.pmatrix[row2 + 1][col2 + 1]
            - self.pmatrix[row1][col2 + 1]
            - self.pmatrix[row2 + 1][col1]
            + self.pmatrix[row1][col1]
        )
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)