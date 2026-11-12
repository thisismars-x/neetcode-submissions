class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        sn, pn = len(s), len(p)

        from functools import cache

        @cache
        def _dfs(i: int, j: int) -> bool:
            if j == pn:
                return i == sn

            is_match = (i < sn and (s[i] == p[j] or p[j] == '.'))

            v = False
            if is_match:
                v = _dfs(i + 1, j + 1)
            
            if v:
                return True

            if j + 1 < pn and p[j + 1] == '*':
                v = (
                    _dfs(i, j + 2) or
                    (is_match and _dfs(i + 1, j)) or 
                    v
                )

            return v

        return _dfs(0, 0)