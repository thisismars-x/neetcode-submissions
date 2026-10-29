class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        n = len(digits)
        for i in range(n):
            l = n - i - 1
            s = digits[l] + carry 
            carry = s // 10
            digits[l] = s % 10
        
        if carry:
            digits.insert(0, carry)

        return digits