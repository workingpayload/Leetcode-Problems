class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False
        
        number_open, number_options, number_unlocked = 0, 0, 0
        for i in range(len(s)):
            if locked[i] == '0':
                if number_open > 0:
                    number_options += 1
                    number_open -= 1
                else:
                    number_unlocked += 1
            else:    
                if s[i] == '(':
                    number_open += 1
                else:
                    if number_open > 0:
                        number_open -= 1
                    elif number_options > 0:
                        number_options -= 1
                        number_unlocked += 1
                    elif number_unlocked > 0:
                        number_unlocked -= 1
                    else:
                        return False
                
        if number_open > 0:
            return False
        
        return True