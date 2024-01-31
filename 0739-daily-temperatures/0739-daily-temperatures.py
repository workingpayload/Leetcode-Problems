class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        
        s, days = [], [0] * len(temp)
        
        for i,t in enumerate(temp):
            while s and t > temp[s[-1]]:
                days[s.pop()] = i-s[-1]
            s.append(i)
        
        return days