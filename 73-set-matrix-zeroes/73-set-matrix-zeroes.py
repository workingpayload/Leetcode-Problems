class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        c = 1
        row = len(matrix)
        column = len(matrix[0])
        
        for i in range(0,row):
            if matrix[i][0]==0:
                c=0
            for j in range(1,column):
                if matrix[i][j]==0:
                    matrix[i][0]=matrix[0][j]=0
                    
                    
        for i in range(row-1,-1,-1):           
                for j in range(column-1,0,-1):
                    if matrix[i][0]==0 or matrix[0][j]==0:
                        matrix[i][j]=0
                if c==0:
                    matrix[i][0]=0
                
                    
        