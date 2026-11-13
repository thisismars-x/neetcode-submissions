class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        length = mountainArr.length()
        lo, hi = 1, length - 2

        while lo <= hi:
            mid = (lo + hi) // 2
            l, m, r = mountainArr.get(mid - 1), mountainArr.get(mid), mountainArr.get(mid + 1)
            if l < m < r:
                lo = mid + 1
            elif l > m > r:
                hi = mid - 1
            else:
                break

            
        peak = mid
        lo, hi = 0, peak - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            v = mountainArr.get(mid)

            if v == target:
                return mid

            if v < target:
                lo = mid + 1
            else:
                hi = mid - 1


        lo, hi = peak, length - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            v = mountainArr.get(mid)

            if v == target:
                return mid
            
            if v > target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1