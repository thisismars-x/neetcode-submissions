class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = set()

        for i in range(1, len(nums) - 1):
            lo, mid, up = i - 1, i, len(nums) - 1

            rsum = -nums[lo]
            while mid < up:
                if nums[mid] + nums[up] == rsum:
                    res.add(
                        # tuple(((nums[lo], nums[mid], nums[up])))
                        (nums[lo], nums[mid], nums[up])
                    )
                    up -= 1 
                    mid += 1
                elif nums[mid] + nums[up] > rsum:
                    up -= 1
                else:
                    mid += 1

        return [list(x) for x in res]