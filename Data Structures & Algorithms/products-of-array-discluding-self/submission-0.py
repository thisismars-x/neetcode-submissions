class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_present = 0
        prod_of_all = 1

        for n in nums:
            if n == 0:
                zero_present += 1
                continue
            prod_of_all *= n

        output = []
        for i in range(len(nums)):
            
            # check if zero is present first
            if zero_present > 1:
                output.append(0)
                continue

            if zero_present == 1:
                if nums[i] == 0:
                    output.append(prod_of_all)
                else:
                    output.append(0)
                continue

            if zero_present == 0:
                output.append(prod_of_all // nums[i])




        return output