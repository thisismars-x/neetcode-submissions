class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m, n = len(word1), len(word2)
        table = {}

        def _dfs(i: int, j: int):
            if (i, j) in table: return table[(i, j)]
            if i == m: return n - j
            if j == n: return m - i

            if word1[i] == word2[j]:
                table[(i, j)] = _dfs(i + 1, j + 1)
            else:
                table[(i, j)] = min(
                    _dfs(i + 1, j),
                    _dfs(i, j + 1),
                    _dfs(i + 1, j + 1)
                ) + 1
            
            return table[(i, j)]

        return _dfs(0, 0)