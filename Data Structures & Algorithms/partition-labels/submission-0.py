class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        final = {}
        for i, c in enumerate(s):
            final[c] = i # last index of this char

        size = 0
        end = 0
        res = []

        for i, c in enumerate(s):
            size += 1
            end = max(end, final[c])

            if i == end:
                res.append(size)
                size = 0

        return res
        