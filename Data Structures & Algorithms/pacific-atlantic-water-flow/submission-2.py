class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # for each cell at the border, do a dfs and see if you can reach the other border
        r, c = len(heights), len(heights[0])
    
        def _dfs(i: int, j: int, visited: set[tuple[int, int]]):
            visited.add((i, j))
            
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                i2, j2 = i + di, j + dj
                if 0 <= i2 < r and 0 <= j2 < c and heights[i2][j2] >= heights[i][j] and (i2, j2) not in visited:
                    _dfs(i2, j2, visited)
                    
        pacific, atlantic = set(), set()
        for i in range(r):
            _dfs(i, c - 1, atlantic)
            _dfs(i, 0, pacific)
        
        for i in range(c):
            _dfs(r - 1, i, atlantic)
            _dfs(0, i, pacific)
        
        return list(pacific & atlantic)