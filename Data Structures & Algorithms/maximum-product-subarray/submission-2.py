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
        ans = _max = _min = nums[0]

        for num in nums[1:]:
            if num < 0:
                _max, _min = _min, _max # mul with negative can make _max _min and _min _max


            _max = max(num, _max * num)
            _min = min(num, _min * num)
            ans = max(ans, _max)

        return ans