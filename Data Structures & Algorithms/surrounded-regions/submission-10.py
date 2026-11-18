class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        # from the edge of the board start a graph search, and make all 'O' 'S'
        r, c = len(board), len(board[0])
        
        def _dfs(i: int, j: int):
            if not board[i][j] == 'O': return 
            stack = [ (i, j) ]
            board[i][j] = 'S'
            
            while stack:
                i, j = stack.pop()
                
                for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    i2, j2 = i + di, j + dj
                    if 0 <= i2 < r and 0 <= j2 < c and board[i2][j2] == 'O':
                        board[i2][j2] = 'S'
                        stack.append((i2, j2))
            
        for i in range(r):
            _dfs(i, c - 1)
            _dfs(i, 0)
            
        for i in range(c):
            _dfs(r - 1, i)
            _dfs(0, i)
            
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                    
                if board[i][j] == 'S':
                    board[i][j] = 'O'