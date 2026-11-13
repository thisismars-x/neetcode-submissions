class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        from bisect import bisect_left, insort
        pos = bisect_left(arr, x)

        n = len(arr)
        l, r = pos - 1, pos

        res = []
        while k and (l >= 0 or r < n):
            if l >= 0 and r < n:
                if abs(arr[l] - x) <= abs(arr[r] - x):
                    insort(res, arr[l])
                    l -= 1
                else:
                    insort(res, arr[r])
                    r += 1

            elif l >= 0:
                insort(res, arr[l])
                l -= 1
            else:
                insort(res, arr[r])
                r += 1

            k -= 1

        return res
