class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        from functools import cache

        @cache
        def _dfs(rem: str | None, word: str) -> bool:
            if not rem: return True
            if len(rem) >= len(word) and rem[:len(word)] == word:
                if any((_dfs(rem[len(word):], x) for x in wordDict)):
                    return True

            return False

        return any((_dfs(s, w) for w in wordDict))