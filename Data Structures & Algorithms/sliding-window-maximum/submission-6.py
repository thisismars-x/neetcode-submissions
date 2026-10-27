class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []

        from heapq import heappush_max as heappush, heappop_max as heappop
        heap = []

        for i in range( len(nums) ):
            heappush(heap, (nums[i], i))

            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heappop(heap)

                res.append(heap[0][0])
        return res