class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def _len_palindrome(l: int, r: int) -> tuple[int, int]:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            l += 1
            r -= 1
            return (l, r)

        max_len = 1
        l, r = 0, 0
        for i in range(len(s)):
            l1, r1 = _len_palindrome(i, i)
            l2, r2 = 0, 0
            if i + 1 < len(s):
                l2, r2 = _len_palindrome(i, i + 1)

            if r1 - l1 + 1 > max_len:
                l, r = l1, r1
                max_len = r1 - l1 + 1
            if r2 - l2 + 1 > max_len:
                l, r = l2, r2
                max_len = r2 - l2 + 1

        return s[l: r + 1]
