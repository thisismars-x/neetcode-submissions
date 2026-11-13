class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        MARK_FOR_DELETION = None

        l, r = 0, 1
        while l < len(nums) and r < len(nums):
            if nums[l] == nums[r]:
                nums[l] = MARK_FOR_DELETION
            l, r = l + 1, r + 1


        nums[:] = [ x for x in nums if x is not None ] 
        return len(nums)
