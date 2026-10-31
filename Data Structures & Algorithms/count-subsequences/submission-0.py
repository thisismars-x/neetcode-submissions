class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        sn, tn = len(s), len(t)

        from functools import cache
        
        @cache
        def _dfs(i: int, j: int) -> int:
            if j == tn:
                return 1
            if i == sn:
                return 0

            # now at ith index, you have the choice to include or exclude
            # include is only possible if both indexes give same char
            res = _dfs(i + 1, j)
            if s[i] == t[j]:
                res += _dfs(i + 1, j + 1)

            return res

        return _dfs(0, 0)