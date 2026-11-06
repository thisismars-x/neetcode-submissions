class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        left, stack = [-1] * n, []
        
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]

            stack.append(i)

        right, stack = [n] * n, []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        m = 0
        for i in range(n):
            l = left[i] + 1
            r = right[i] - 1
            m = max(
                m, 
                heights[i] * (r - l + 1)
            )
        return m