class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def contains_dup(arr: list[str]) -> bool:
            return not (len(list(x for x in arr if x != ".")) == len(set((x for x in arr if x != "."))))

        # check row, col then each box
        i,j=0,0
        for k in range(9):
            # create array view first
            arr = []
            arr.extend(board[i][j:j+3])
            arr.extend(board[i + 1][j:j+3])
            arr.extend(board[i + 2][j:j+3])
            if contains_dup(arr): return False

            i += 3
            if i > 8:
                i = 0
                j += 3

        # check col
        for i in range(9):
            col = []
            for j in range(9):
                col.append(board[j][i])
            
            if contains_dup(col): return False

        for i in range(9):
            if contains_dup(board[i]): return False


        return True