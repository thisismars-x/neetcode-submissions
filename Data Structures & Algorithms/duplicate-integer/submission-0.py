class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums: return False
        from collections import Counter
        return Counter(nums).most_common(1)[0][1] > 1