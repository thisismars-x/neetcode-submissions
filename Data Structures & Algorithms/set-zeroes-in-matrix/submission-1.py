class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        SENTINEL = None
        
        r, c = len(matrix), len(matrix[0])

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    
                    # change entire row
                    for k in range(c):
                        if matrix[i][k] != 0:
                            matrix[i][k] = SENTINEL

                    # change entire col
                    for k in range(r):
                        if matrix[k][j] != 0:
                            matrix[k][j] = SENTINEL
        
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == SENTINEL:
                    matrix[i][j] = 0