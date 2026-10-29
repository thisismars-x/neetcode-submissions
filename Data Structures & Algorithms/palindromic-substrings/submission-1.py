
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