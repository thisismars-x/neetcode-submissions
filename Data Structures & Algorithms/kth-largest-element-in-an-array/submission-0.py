class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heapq.heapify_max(nums)

        for _ in range(k - 1):
            _ = heapq.heappop_max(nums)

        return heapq.heappop_max(nums)
        