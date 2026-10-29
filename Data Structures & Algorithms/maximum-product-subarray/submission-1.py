# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
        
#         # solving using dp
#         n = len(nums)
#         table = [ [0] * n for _ in range(n) ]
#         for i in range(n):
#             table[i][i] = nums[i]

#         max_prod = max(nums)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 table[i][j] = table[i][j-1] * nums[j]
#                 max_prod = max(max_prod, table[i][j])

#         return max_prod

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = ans = nums[0]

        for x in nums[1:]:
            if x < 0:
                max_prod, min_prod = min_prod, max_prod

            max_prod = max(x, max_prod * x)
            min_prod = min(x, min_prod * x)

            ans = max(ans, max_prod)

        return ans