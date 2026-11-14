class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        from functools import cache
        
        @cache
        def _dfs(i: int, s: bool) -> int:
            if i == len(arr) - 1:
                return 1

            res = 1
            if (
                (s and arr[i] < arr[i + 1]) or
                (not s and arr[i] > arr[i + 1])
            ):
                res = 1 + _dfs(i + 1, not s)

            return res

        res = 1
        for i in range(len(arr)):
            res = max(res, _dfs(i, True), _dfs(i, False))
        return res