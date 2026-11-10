class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        tsum = sum(matchsticks)
        if tsum % 4 != 0:
            return False
        asum = tsum // 4

        matchsticks.sort(reverse=True)
        if matchsticks[0] > asum:
            return False


        table = [0] * 4

        def _ms(i: int):
            if i == len(matchsticks):
                return all(x == asum for x in table)

            for side in range(4):
                if table[side] + matchsticks[i] > asum:
                    continue

                table[side] += matchsticks[i]

                if _ms(i + 1):
                    return True

                table[side] -= matchsticks[i]
                if table[side] == 0:
                    break

            return False

        return _ms(0)
