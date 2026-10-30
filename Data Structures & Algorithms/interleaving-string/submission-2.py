class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not (len(s1) + len(s2) == len(s3)):
            return False
        
        table = {}

        def _dfs(i: int, j: int, k: int) -> bool:
            if k == len(s3):
                return i == len(s1) and j == len(s2)

            if (i, j) in table:
                return table[(i, j)]

            can = False
            if i < len(s1) and s1[i] == s3[k]:
                can = _dfs(i + 1, j, k + 1)
            if not can and j < len(s2) and s2[j] == s3[k]:
                can = _dfs(i, j + 1, k + 1)

            table[(i, j)] = can
            return can

        return _dfs(0, 0, 0)