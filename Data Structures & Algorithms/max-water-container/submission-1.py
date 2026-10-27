class Solution:
    def maxArea(self, heights: List[int]) -> int:
        import sys

        n = len(heights)
        left, right = 0, n - 1
        max_height = -sys.maxsize

        while left < right:
            curr_height = (right - left) * min(heights[left], heights[right])
            max_height = max(max_height, curr_height)

            if heights[left] < heights[right]: left += 1
            else: right -= 1
            
        return max_height