class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # this is dfs solvable
        res = []


        def _dfs(s: list[str], nop: int, ncl: int):
            if nop > n or ncl > nop:
                return

            if nop == n and ncl == n:
                res.append(''.join(s))
                return

            ## try appending ')' 
            s.append(')')
            _dfs(s, nop, ncl + 1)
            s.pop()

            ## try appending '('
            s.append('(')
            _dfs(s, nop + 1, ncl)
            s.pop()

        _dfs([], 0, 0)
        return res
        