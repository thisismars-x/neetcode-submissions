class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        from functools import cache
        words = set(dictionary)

        @cache
        def _dfs(i: int) -> int:
            if i == len(s):
                return 0

            ans = 1 + _dfs(i + 1)

            for w in words:
                if s.startswith(w, i):
                    ans = min(ans, _dfs(i + len(w)))

            return ans

        return _dfs(0)
        