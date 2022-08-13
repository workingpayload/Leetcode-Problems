class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(0,len(matrix)):
            for j in range(0,i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
                
                
        for k in range(0,len(matrix)):
            matrix[k] = matrix[k][::-1]
            
        
        