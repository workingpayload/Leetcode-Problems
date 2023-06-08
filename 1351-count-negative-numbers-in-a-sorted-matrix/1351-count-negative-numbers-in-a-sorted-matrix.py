class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        cnt = 0
        n,m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] < 0:
                    cnt += (n - i) * (m-j) 
                    m = j
                    break
            if m == 0:
                break
        return cnt