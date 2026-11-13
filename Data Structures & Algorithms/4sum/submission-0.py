class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = set()
        
        # similar to 3Sum i would assume?

        n = len(nums)

        for i in range(n - 4):
            required_sum = target - nums[i]

            # now from here on solve like the threesome problem?

            for j in range(i + 2, n - 1):
                lo, mid, up = j - 1, j, n - 1

                # of these only lo is fixed?

                required_sum -= nums[lo]

                while mid < up:
                    if nums[mid] + nums[up] == required_sum:
                        res.add(tuple((nums[lo], nums[mid], nums[up])))
                        mid += 1
                        up -= 1 

                    elif nums[mid] + nums[up] > required_sum:
                        up -= 1
                    else:
                        mid += 1

        return [ list(x) for x in res ]
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
                        