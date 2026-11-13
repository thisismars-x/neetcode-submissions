class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        return [c for c, i in Counter(nums).most_common() if i > len(nums) // 3]
        