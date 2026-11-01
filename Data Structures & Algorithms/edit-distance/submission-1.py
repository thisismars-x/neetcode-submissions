class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n1, n2 = len(word1), len(word2)
        from functools import cache

        @cache
        def _dfs(i: int, j: int) -> int:
            if i == n1:
                return n2 - j
            if j == n2:
                return n1 - i

            if word1[i] == word2[j]:
                return _dfs(i + 1, j + 1)
            else:
                return min(
                    _dfs(i + 1, j),
                    _dfs(i, j + 1),
                    _dfs(i + 1, j + 1)
                ) + 1

        return _dfs(0, 0)



















        
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