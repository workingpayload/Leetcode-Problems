class Solution:
    def interpret(self, command: str) -> str:
        
        new = ""
        
        
        for i in range(len(command)-1):
            
            if command[i]=="G":
                new+="G"
            elif command[i]=="(" and command[i+1]==")":
                new+="o"
            elif command[i]=="(" and command[i+1]=="a":
                new+="al"
                
        if command[-1]=="G":
            new+="G"
            
        return new    
                
            
                
        