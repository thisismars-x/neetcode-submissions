class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        def _find(k: int):
            if k == 0:
                return False
            
            # take a k-size window and go
            n = len(nums) - 1
            for i in range(n - k + 1):
                s, e = i, i + k
                if nums[s] == nums[e]:
                    return True
    
            return False

        for k in range(1, k + 1):
            if _find(k):
                return True

        return False