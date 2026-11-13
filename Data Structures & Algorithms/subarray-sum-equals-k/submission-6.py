class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        from collections import defaultdict
        d = defaultdict(int)

        d[0] = 1

        tc = 0
        curr = 0
        for num in nums:
            curr += num
            tc += d[curr - k]
            d[curr] += 1

        return tc
            

