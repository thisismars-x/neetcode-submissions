class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()

        n = len(nums)

        for i in range(n - 3):
            required_sum = target - nums[i]

            for j in range(i + 1, n - 2):
                remaining = required_sum - nums[j]

                lo, up = j + 1, n - 1

                while lo < up:
                    curr = nums[lo] + nums[up]

                    if curr == remaining:
                        res.add((nums[i], nums[j], nums[lo], nums[up]))
                        lo += 1
                        up -= 1

                    elif curr > remaining:
                        up -= 1
                    else:
                        lo += 1

        return [list(x) for x in res]
                        