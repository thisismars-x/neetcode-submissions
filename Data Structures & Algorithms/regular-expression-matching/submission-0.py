class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        from functools import cache

        @cache
        def _dfs(i: int, j: int) -> int:
            if len(p) == j:
                return len(s) == i

            match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            # handle '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                return _dfs(i, j + 2) or (match and _dfs(i + 1, j))

            return _dfs(i + 1, j + 1) if match else False

        return _dfs(0, 0)