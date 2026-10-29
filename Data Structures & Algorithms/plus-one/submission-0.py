class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        for i in range(len(digits)):
            l = len(digits) - i - 1
            s = digits[l] + carry 
            carry = s // 10
            digits[l] = s % 10
        
        if carry:
            digits.insert(0, carry)

        return digits