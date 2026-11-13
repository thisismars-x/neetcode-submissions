
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        from functools import cache

        @cache
        def dfs(w: int) -> list[str]:
            if w == len(s):
                return [""]

            result = []

            for word in wordDict:
                if s.startswith(word, w):
                    for suffix in dfs(w + len(word)):
                        result.append(
                            word if not suffix else word + " " + suffix
                        )

            return result

        return dfs(0)