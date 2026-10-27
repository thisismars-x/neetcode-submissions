class Solution:
    def trap(self, height: List[int]) -> int:

        # you need to know max height till you get here on left and right side both
        n = len(height)
        left_max, right_max = height[0], height[n - 1]

        total = 0
        l, r = 0, n - 1

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                total += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                total += right_max - height[r]

        return total


