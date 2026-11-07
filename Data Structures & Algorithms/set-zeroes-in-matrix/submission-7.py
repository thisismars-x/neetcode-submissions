class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        r, c = len(matrix), len(matrix[0])

        row_z = False
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        row_z = True
                    matrix[0][j] = 0


        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(r):
                matrix[i][0] = 0

        if row_z:
            for j in range(c):
                matrix[0][j] = 0