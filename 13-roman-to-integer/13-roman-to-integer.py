class Solution:
    def romanToInt(self, s: str) -> int:
        rm = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        rm2 = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        
        q = 0
        
        for k, v in rm2.items():
            if k in s:
                s = s.replace(k, "")
                q += v
                
        for i in s:
            q += rm[i]
        
        return q
        