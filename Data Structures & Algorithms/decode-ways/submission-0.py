class Solution:
    def numDecodings(self, s: str) -> int:
        from functools import cache

        @cache
        def _dfs(i: int):
            if i == len(s):
                return 1

            if s[i] == "0":
                return 0

            res = _dfs(i + 1)
            if i + 1 < len(s) and 0 <= int(s[i:i+2]) <= 26:
                res += _dfs(i + 2)

            return res

        return _dfs(0)