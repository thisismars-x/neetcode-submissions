class Solution:
    def checkValidString(self, s: str) -> bool:
        
        # solve this useing dp
        from functools import cache

        @cache
        def _dfs(i: int, nopen: int) -> bool:
            if i >= len(s):
                return nopen == 0

            if nopen < 0:
                return False

            if s[i] == '(':
                return _dfs(i + 1, nopen + 1)
            
            if s[i] == ')':
                return _dfs(i + 1, nopen - 1)

            else: # star '*' can mean anything
                return (
                    _dfs(i + 1, nopen + 1) or
                    _dfs(i + 1, nopen - 1) or
                    _dfs(i + 1, nopen)
                )

        return _dfs(0, 0)