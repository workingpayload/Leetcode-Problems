class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1, n2 = len(s1), len(s2)                  
                                                    
        ctr1, ctr2 = Counter(s1), Counter(s2[:n1])  
                                                   
        for i in range(n1,n2):                     
            if ctr1 == ctr2: return True           
                                                    
            ctr2[s2[i-n1]]-= 1                     
            ctr2[s2[i   ]]+= 1

        return ctr1 == ctr2