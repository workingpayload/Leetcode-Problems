class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posdig = set()
        negdig = set()
        
        res = []
        
        board = [["."]*n for i in range(n)]
        
        def backtrack(r):
            
            if r==n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                
                if c in cols or (r+c) in posdig or (r-c) in negdig:
                    continue
                    
                cols.add(c)
                posdig.add(r+c)
                negdig.add(r-c)
                board[r][c]="Q"
                
                backtrack(r+1)
                
                cols.remove(c)
                posdig.remove(r+c)
                negdig.remove(r-c)
                board[r][c]="."
                
        backtrack(0)
        return res
                
                
                
                
        