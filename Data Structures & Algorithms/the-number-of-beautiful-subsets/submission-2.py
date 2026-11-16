class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        tc = 0

        for i in range(1 << len(nums)):
            tmp = []
            status = False
            for j in range(len(nums)):
                if (i & (1 << j)):
                    if tmp:
                        if any((abs(x - nums[j]) == k) for x in tmp):
                            status = True
                            break
                    tmp.append(nums[j])

            if tmp and not status:
                tc += 1


        return tc
