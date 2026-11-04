class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        found = [False, False, False]  

        for t in triplets:
            if any(t[i] > target[i] for i in range(3)):
                continue

            for i in range(3):
                if t[i] == target[i]:
                    found[i] = True

        return all(found)