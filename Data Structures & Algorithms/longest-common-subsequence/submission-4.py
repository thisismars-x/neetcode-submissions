class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        if len(text1) > len(text2):
            text1, text2 = text2, text1

        table = [ [ 0 ] * ( 1 + len(text2) ) for _ in range(1 + len(text1)) ]

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):

                if text1[i - 1] == text2[j - 1]:
                    table[i][j] = table[i - 1][j - 1] + 1
                else:
                    table[i][j] = max(table[i][j - 1], table[i - 1][j])

        return table[-1][-1]

