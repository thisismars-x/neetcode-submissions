class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        c = columnNumber

        if c == 0: return ''

        return self.convertToTitle((c - 1) // 26) + chr( (c - 1) % 26 + ord('A') )
        