class Solution:
    def countSubstrings(self, s: str) -> int:

        def _expandpali(l: int, r: int) -> int:
            npali = 0

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                npali += 1

            return npali

        tc = 0
        for i in range(len(s)):
            tc += _expandpali(i, i)
            if i < len(s):
                tc += _expandpali(i, i + 1)

        return tc
            
        