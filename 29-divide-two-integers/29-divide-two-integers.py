import math
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1: return 2147483647
        a = dividend / divisor
        if a >= 0:
            return math.floor(a)
        if a < 0:
            return math.ceil(a)
       