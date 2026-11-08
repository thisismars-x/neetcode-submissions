class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        from functools import cache
        @cache
        def _sg(s: int, e: int) -> int:
            if s > e:
                return 0

            nstones = e - s
            l, r = 0, 0
            if not (nstones & 1):
                l, r = piles[s], piles[r]

            return max(_sg(s + 1, e) + l, _sg(s, e - 1) + r)

        score = _sg(0, len(piles) - 1)
        return score > sum(piles) - score
