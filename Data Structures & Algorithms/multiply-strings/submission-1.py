class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        table = {str(i): i for i in range(10)}
        table2 = {i: str(i) for i in range(10)}

        def _str_to_num(x: str) -> int:
            res = 0

            i = 0
            while x:
                lowest = table[x[-1]]
                x = x[:-1]
                res += (lowest * (10 ** i))
                i += 1

            return res

        def _num_to_str(num: int) -> str:
            res = ''

            while num:
                lowest = num % 10
                num //= 10
                res += table2[lowest]

            return res[::-1] if res[::-1] else '0'

        return _num_to_str(_str_to_num(num1) * _str_to_num(num2))