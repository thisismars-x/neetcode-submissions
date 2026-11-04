class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        from functools import cache

        @cache
        def _dfs(i: int) -> bool:
            if i == len(s):
                return True

            # match the words in the dictionary
            for word in wordDict:
                if len(word) <= len(s) - i:
                    if word == s[i:i+len(word)]:
                        if _dfs(i + len(word)):
                            return True

            return False

        return _dfs(0)