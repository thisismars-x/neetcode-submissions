class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # does this work

        n1, n2 = len(nums1), len(nums2)
        i, j = 0, 0

        med_1 = med_2 = 0
        for k in range( (n1 + n2) // 2 + 1 ):
            med_2 = med_1
            if i < n1 and j < n2:
                if nums1[i] > nums2[j]:
                    med_1 = nums2[j]
                    j += 1
                else:
                    med_1 = nums1[i]
                    i += 1
            elif i < n1:
                med_1 = nums1[i]
                i += 1
            else:
                med_1 = nums2[j]
                j += 1

        if (n1 + n2) % 2: return float(med_1)
        else: return (med_1 + med_2) / 2
            
