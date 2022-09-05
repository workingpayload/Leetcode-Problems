class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        
        ss = ""
        res= []
        
        for i in s:
            if i not in ss:
                ss+=i
                res.append(ss)
                
            else:
                index = ss.find(i)
                ss = ss[index+1:]+i
                
        return max([len(x) for x in res])        
        
        