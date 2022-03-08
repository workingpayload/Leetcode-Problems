class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        mapper = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}
        return str(Solution.convertToInteger(num1, mapper) * Solution.convertToInteger(num2, mapper))
    
    
    def convertToInteger(num, mapper):
        number = 0
        for i in range(len(num)):
            number += mapper[num[i]] * 10 ** (len(num) - i - 1)
        return number