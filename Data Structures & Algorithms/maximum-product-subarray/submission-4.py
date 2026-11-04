class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        mx = mn = ans = nums[0]

        for num in nums[1:]:
            if num < 0:
                mx, mn = mn, mx

            mx = max(num, mx * num)
            mn = min(num, mn * num)
            ans = max(ans, mx)

        return ans
