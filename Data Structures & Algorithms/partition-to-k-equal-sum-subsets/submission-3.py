class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if int(s / k) != s // k:
            return False

        ass = s // k
        used = [False] * len(nums)

        def _bt(i: int, k: int, ss: int) -> bool:
            if k == 0:
                return True

            if ss == ass:
                return _bt(0, k - 1, 0)

            for j in range(i, len(nums)):
                if used[j] or ss + nums[j] > ass:
                    continue
                used[j] = True
                if _bt(j + 1, k, ss + nums[j]):
                    return True

                used[j] = False
            return False

        return _bt(0, k, 0)
        