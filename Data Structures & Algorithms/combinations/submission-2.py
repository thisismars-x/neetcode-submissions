class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []

        def _combs(i: int, curr: list[int]):
            # if i > n:
            if len(curr) == k:
                res.append(curr[:])
                return
            if i > n:
                return

            curr.append(i)
            _combs(i + 1, curr)

            curr.pop()
            _combs(i + 1, curr)

        _combs(1, [])
        return res
            
