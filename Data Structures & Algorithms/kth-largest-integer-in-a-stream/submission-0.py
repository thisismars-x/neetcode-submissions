class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)[::-1]
        self.k = k
       

    def add(self, val: int) -> int:
        from bisect import insort
        from operator import neg
        insort(self.nums, val, key=neg)
        return self.nums[self.k-1]

