class Solution:
    def isValid(self, s: str) -> bool:
            counter = 0
            
            valids = ['()','{}','[]']
            
            
            for i in valids:
                if i in s:
                    s = s.replace(i,'')
                    counter+=1
                    
                    
            if s == '':
                return True
            
            elif s!='' and counter==0:
                return False
            
            else:
                return self.isValid(s)
            