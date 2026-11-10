class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def _check_pali(l: int, r: int, already_del: bool) -> bool:
            while l < r:
                if s[l] != s[r]:
                    if not already_del:
                        return _check_pali(l + 1, r, True) or _check_pali(l, r - 1, True)
                    else:
                        return False
                
                l += 1
                r -= 1

            return True

        
        return _check_pali(0, len(s) - 1, False)