import re
class Solution:
    def myAtoi(self, s: str) -> int:
        rslt = re.compile("\s*?([+-]?\d+)").match(s)
        return max(min(int(rslt.group(1)), 2 ** 31 - 1), -2 ** 31) if rslt else 0
        