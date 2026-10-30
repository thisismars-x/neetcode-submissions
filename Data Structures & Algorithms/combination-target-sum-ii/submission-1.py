class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n = len(candidates)
        candidates.sort()
        res = []

        def _dfs(i: int, k: int, v: list[int]):
            if k == 0:
                res.append(v.copy())
                return
            
            if k < 0 or i == n:
                return

            for j in range(i, n):
                if j > i and candidates[j] == candidates[j - 1]: continue
                if candidates[j] > k: break
                v.append(candidates[j])
                _dfs(j + 1 ,k - candidates[j], v)
                v.pop()

        _dfs(0, target, [])
        return res


        # naive way
        # n = len(candidates)
        # res = set()

        # def _dfs(i: int, k: int, v: list[int]):
        #     if k == 0:
        #         res.add(tuple(v))
        #         return
        #     if k < 0:
        #         return
        #     if i == n:
        #         return

        #     v.append(candidates[i])
        #     _dfs(i + 1, k - candidates[i], v)
        #     v.pop()

        #     # do not take
        #     _dfs(i + 1, k, v)

        # _dfs(0, target, [])
        # return list( (list(s) for s in res) )