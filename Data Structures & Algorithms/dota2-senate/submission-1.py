class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        sen = list(senate)
        c, i = 0, 0       

        while i < len(sen):
            _c = sen[i]

            if _c == 'R':
                if c < 0: sen.append('D')
                c += 1
            else:
                if c > 0: sen.append('R')
                c -= 1

            i += 1

        return 'Radiant' if c > 0 else 'Dire'