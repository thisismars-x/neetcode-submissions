class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        c = {}
        def _dfs(rem: str | None, word: str) -> bool:
            if not rem: return True
            if (rem, word) in c: return c[(rem, word)]
            if len(rem) >= len(word) and rem[:len(word)] == word:
                if any((_dfs(rem[len(word):], x) for x in wordDict)):
                    c[(rem, word)] = True
                    return True

            c[(rem, word)] = False
            return False

        return any((_dfs(s, w) for w in wordDict))