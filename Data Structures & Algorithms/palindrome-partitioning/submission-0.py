class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        v = []
        def _dfs(i: int, j: int):
            if j >= len(s):
                if i == j:
                    res.append(v.copy())
                return
            
            # check if palindrome
            l, r = i, j
            is_p = True
            while l < r:
                if s[l] != s[r]:
                    is_p = False
                    break
                l += 1
                r -= 1

            if is_p:
                v.append(s[i:j+1])
                _dfs(j + 1, j + 1)
                v.pop()
            
            _dfs(i, j + 1)
        
        _dfs(0, 0)
        return res