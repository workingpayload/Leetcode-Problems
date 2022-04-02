class Solution:
    def palindrome(s,l,r):
            while(l<r):
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True    
                
    def validPalindrome(self, s: str) -> bool:
        
        if s==s[::-1]:
            return True
        l = 0
        r = len(s)-1
        
        while(l<r):
            if s[l]==s[r]:
                l+=1
                r-=1
                
            elif s[l]!=s[r]:
                return Solution.palindrome(s,l+1,r) or Solution.palindrome(s,l,r-1)
            
        