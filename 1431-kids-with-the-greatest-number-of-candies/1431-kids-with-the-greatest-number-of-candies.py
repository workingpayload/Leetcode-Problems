class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        p = max(candies)
        boolist = []
        
        for i in range(len(candies)):
            if (candies[i]+extraCandies)>=p:
                boolist.append(True)
            else:
                boolist.append(False)
                
                
        return boolist        
        
        