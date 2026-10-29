class Solution:
    def longestPalindrome(self, s: str) -> str:

        # we can save memory by using the earlier palindrome trick
        n = len(s)
        start, end = 0, 0
        def _expand(l: int, r: int):
            nonlocal start, end
            while 0 <= l and r < n and s[l] == s[r]:
                l -= 1 
                r += 1
            l += 1
            r -= 1
            if r - l + 1 > end - start + 1:
                start, end = l, r

        for i in range(n):
            _expand(i, i), _expand(i, i + 1)

        return s[start:end+1]

        n = len(s)
        table = [ [False] * n for _ in range(n) ]

        curr_max = 1
        start, end = 0, 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i + 1 <= 3 or table[i + 1][j - 1]:
                        table[i][j] = True
                        curr_len = j - i + 1
                        if curr_len > curr_max:
                            curr_max = curr_len
                            start, end = i, j

        return s[start: end + 1]
        