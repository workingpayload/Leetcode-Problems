class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
    
        """
        m, n = len(board), len(board[0])
        dirs = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
        for i in range(m):
            for j in range(n):
                livecount = 0
                for r, c in dirs:
                    nr, nc = i + r, j + c
                    if 0 <= nr < m and 0 <= nc < n and abs(board[nr][nc]) == 1:
                        livecount += 1
                if board[i][j] == 1:
                    if livecount < 2 or livecount > 3:   
                        board[i][j] = -1
                else:
                    if livecount == 3:  
                        board[i][j] = 2
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:    board[i][j] = 1
                elif board[i][j] == -1: board[i][j] = 0
        