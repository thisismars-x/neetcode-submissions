class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # try:
        #     return nums.index(target)
        # except:
        #     return -1

        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            if nums[lo] <= nums[hi]:
                break

            mid = (lo + hi) // 2

            # can i reverse the condition
            if nums[lo] <= nums[mid]: lo = mid + 1
            else: hi = mid

        arr1, arr2 = nums[:lo], nums[lo:]

        blo, bhi = 0, len(arr1) - 1
        while blo <= bhi:
            mid = (blo + bhi) // 2
            if nums[mid] == target: return mid
            if nums[mid] > target: bhi = mid - 1
            else: blo = mid + 1


        blo, bhi = 0, len(arr2) - 1
        while blo <= bhi:
            mid = (blo + bhi) // 2
            if arr2[mid] == target: return mid + len(arr1)
            if arr2[mid] > target: bhi = mid - 1
            else: blo = mid + 1


        return -1
            
