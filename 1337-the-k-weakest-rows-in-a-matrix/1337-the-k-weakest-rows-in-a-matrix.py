class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        l = []
        
        for i,row in enumerate(mat):
            l.append((sum(row),i))
            
        l.sort()
        
        k_sorted = l[:k]
        
        res = []
        
        for i in k_sorted:
            res.append(i[1])
            
        return res    
            
            
        
        
                    
                
        