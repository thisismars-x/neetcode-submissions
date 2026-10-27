class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        r, c = len(matrix), len(matrix[0])


        lo, hi = 0, r * c - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            _r = mid // c
            _c = mid - (_r * c)

            number = matrix[_r][_c]
            if number == target: return True
            if number > target: hi = mid - 1
            else: lo = mid + 1

        return False