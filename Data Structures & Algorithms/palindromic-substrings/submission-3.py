
class Solution:
    def countSubstrings(self, s: str) -> int:

        tc = 0
        # there can be two types of palindromes:
        # even length and odd length
        for i in range(len(s)):
            # i is the center of the palindrome
            l, r = i, i # for odd length
            while l <= r and 0 <= l and r < len(s) and s[l] == s[r]:
                tc += 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while l <= r and 0 <= l and r < len(s) and s[l] == s[r]:
                tc += 1
                l -= 1
                r += 1

        return tc

        # the dp solution
        table = [ [False] * len(s) for _ in range(len(s)) ]
        tc = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if (j - i <= 2 or table[i + 1][j - 1]):
                        table[i][j] = True
                        tc += 1

        return tc