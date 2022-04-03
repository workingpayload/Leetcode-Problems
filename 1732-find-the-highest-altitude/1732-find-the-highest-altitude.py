class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        num = [0]
        
        for i in range(len(gain)):
            num.append(num[i]+gain[i])
            
        return max(num)    
        