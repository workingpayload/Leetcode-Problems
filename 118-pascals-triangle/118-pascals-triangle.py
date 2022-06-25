class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        mat = []
        for i in range(1,numRows+1):
            mat.append([0]*i)
        for i in range(len(mat)):
            mat[i][0] = 1
            mat[i][i] = 1
        for i in range(2, len(mat)):
            for j in range(1, len(mat[i])-1):
                mat[i][j] = mat[i-1][j-1] + mat[i-1][j]
        return mat