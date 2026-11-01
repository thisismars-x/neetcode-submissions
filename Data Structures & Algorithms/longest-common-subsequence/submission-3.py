class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        if len(text1) > len(text2):
            text1, text2 = text2, text1

        table = [ [0] * len(text2) for _ in range(len(text1)) ]

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    table[i][j] = (table[i - 1][j - 1] if i > 0 and j > 0 else 0) + 1
                else:
                    table[i][j] = max(table[i - 1][j] if i > 0 else 0, table[i][j - 1] if j > 0 else 0)

        return table[-1][-1]
















        if len(text1) > len(text2):
            text1, text2 = text2, text1
        m, n = len(text1), len(text2)

        table = [ [0] * (n + 1) for _ in range(m + 1) ]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    table[i][j] = table[i-1][j-1] + 1
                else:
                    table[i][j] = max(table[i-1][j], table[i][j-1])

        
        return table[-1][-1]