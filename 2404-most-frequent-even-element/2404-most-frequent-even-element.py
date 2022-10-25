class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        
        dic = {}
        
        for i in nums:
            
            if i%2==0:
                if i in dic:
                    dic[i]+=1
                else:
                    dic[i]=1
                    
        if len(dic)==0:
            return -1
                    
                    
        maxi = 0
        
        for i in dic:
            maxi = max(maxi,dic[i])
        
        res = float('inf')
        
        for i in dic:
            if dic[i]==maxi:
                res = min(res,i)
                
        return res       
        