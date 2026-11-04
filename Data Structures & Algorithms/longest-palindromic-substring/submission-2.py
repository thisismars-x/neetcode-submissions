class Solution:
    def longestPalindrome(self, s: str) -> str:

        def _expandpali(l: int, r: int) -> tuple[int, int]:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            l += 1
            r -= 1
            return l, r

        # pali can either be odd or even in length

        max_len = 1
        ml, mr = 0, 0
        for i in range(len(s)):
            l, r = _expandpali(i, i)
            if r - l + 1 > max_len:
                max_len = r - l + 1
                ml, mr = l, r

            if i + 1 < len(s):
                l2, r2 = _expandpali(i, i + 1)
                if r2 - l2 + 1 > max_len:
                    max_len = r2 - l2 + 1
                    ml, mr = l2, r2

        return s[ml:mr + 1]
        