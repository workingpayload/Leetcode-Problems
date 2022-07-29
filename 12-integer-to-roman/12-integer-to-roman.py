class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        mapping = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I',}

        for i in [1000, 100, 10, 1]:
            digit, num = num // i, num % i
            if digit == 0:
                continue
            elif digit <= 3:
                res += mapping[i] * digit
            elif digit == 4:
                res += (mapping[i] + mapping[5 * i])
            elif digit < 9:
                res += (mapping[5 * i] + mapping[i] * (digit - 5))
            elif digit == 9:
                res += (mapping[i] + mapping[10 * i])
        return res