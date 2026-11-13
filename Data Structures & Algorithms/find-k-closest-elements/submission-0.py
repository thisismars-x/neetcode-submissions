class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        from bisect import bisect_left
        pos = bisect_left(arr, x)

        n = len(arr)
        l, r = pos - 1, pos

        res = []
        while k and (l >= 0 or r < n):
            if l >= 0 and r < n:
                if abs(arr[l] - x) <= abs(arr[r] - x):
                    res.append(arr[l])
                    l -= 1
                else:
                    res.append(arr[r])
                    r += 1

            elif l >= 0:
                res.append(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1

            k -= 1

        return sorted(res)