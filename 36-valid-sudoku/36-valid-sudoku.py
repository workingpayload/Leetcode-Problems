class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        #check if rows are valid
        block = [[],[],[],[],[],[],[],[],[]]
        row = 0
        while row < 9:
            num = 0
            while num < 9:
                i = num + 1
            
                while i < 9:
                    if board[row][num] != "." and board[row][num] == board[row][i]:
                        return False
                    i += 1
                if board[row][num] != ".":
                        block[row].append(board[row][num])    
                num += 1
            row += 1
        
        for i in block:
            if len(set(i)) != len(i):
                return False
        
        
        
        #check if columns are valid
        block = [[],[],[],[],[],[],[],[],[]]
        column = 0
        while column < 9:
            num = 0
            while num < 9:
                i = num + 1
            
                while i < 9:
                    if board[num][column] != "." and board[num][column] == board[i][column]:
                        return False
                    i += 1
                if board[num][column] != ".":
                        block[column].append(board[num][column])    
                num += 1
            column += 1
        
        for i in block:
            if len(set(i)) != len(i):
                return False

        
        
        #insert each box into a list in a list and checks if numbers
        #repeat using len(set()) and len()
        block = [[],[],[],[],[],[],[],[],[]]
        sub = []
        
        #first column of 3x3 squares
        row = 0
        box = 0
        start = 0
        end = 3
        boxNum = 0
        
        for y in range(0,9):
            if y < 3:
                boxNum = 0
            elif y < 6:
                boxNum = 1
            else:
                boxNum = 2
            i = 0
            while i < 3:
                if board[row][i] != ".":
                    block[boxNum].append(board[row][i])
                i += 1
            row += 1
        
        #second column of 3x3 squares
        row = 0
        box = 0
        start = 3
        end = 6
        boxNum = 3
        
        for y in range(0,9):
            if y < 3:
                boxNum = 3
            elif y < 6:
                boxNum = 4
            else:
                boxNum = 5
            i = 3
            while 3 <= i < 6:
                if board[row][i] != ".":
                    block[boxNum].append(board[row][i])
                i += 1
            row += 1    
                
        #thrid column of 3x3 squares  
        row = 0
        box = 0
        start = 6
        end = 9
        boxNum = 6
        
        for y in range(0,9):
            if y < 3:
                boxNum = 6
            elif y < 6:
                boxNum = 7
            else:
                boxNum = 8
            i = 6
            while 6 <= i < 9:
                if board[row][i] != ".":
                    block[boxNum].append(board[row][i])
                i += 1
            row += 1    
                
                
        for i in block:
            if len(set(i)) != len(i):
                return False
        
            
        return True