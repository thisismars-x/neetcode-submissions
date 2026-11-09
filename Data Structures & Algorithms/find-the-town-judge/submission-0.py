class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        # looks like a indegree question
        table = [0] * (n + 1)
        table2 = [0] * (n + 1)

        for a, b in trust:
            table[b] += 1
            table2[a] += 1

        res = -1
        for i, (ind, out) in enumerate(zip(table, table2)):
            if ind == n - 1 and out == 0:
                if res == -1:
                    res = i
                else:
                    return -1

        return res
                