class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        n = len(nums)

        ts = 0
        for i in range(1 << n):
            c_xor = 0
            for j in range(n):
                if i & (1 << j):
                    c_xor ^= nums[j]
            ts += c_xor

        return ts