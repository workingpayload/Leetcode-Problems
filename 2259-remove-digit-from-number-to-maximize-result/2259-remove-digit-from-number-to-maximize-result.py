class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
        maxVal = 0
        for i in range(len(number)):
            if number[i] == digit:
                result = int(number[:i] + number[i+1:])
                maxVal = max(maxVal,result)
        return str(maxVal)
        
        
        