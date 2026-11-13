class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        result = []

        from functools import cache

        @cache
        def _dfs(w: int) -> list[str]:
            if w == len(s):
                return [""]

            res = []

            for word in wordDict:
                if s.startswith(word, w):
                    starts = _dfs(w + len(word))

                    for suffix in starts:
                        if suffix:
                            res.append(word + " " + suffix)
                        else:
                            res.append(word)

            return res

        return _dfs(0)