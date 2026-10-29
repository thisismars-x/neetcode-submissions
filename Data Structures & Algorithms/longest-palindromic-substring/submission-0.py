class Solution:
    def longestPalindrome(self, s: str) -> str:

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
        