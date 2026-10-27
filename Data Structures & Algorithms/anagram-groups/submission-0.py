class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)

        # this problem should be solvable by hashing
        from collections import defaultdict
        d = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            d[sorted_s].append(s)

        return list(d.values())