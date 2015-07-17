class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudoku(self, board):
    	candidates = [];
    	for i in range(0, 9):
    		for j in range(0, 9):
    			if(board[i][j] == '.'):
    				candidates.append(i*9+j);
    	length = len(candidates);
    	self.sudokuSolver(board, candidates, 0, length);
    	return;
    
    def sudokuSolver(self, board, candidates, index, length):
    	if(index == length):
    		return True;
    	num = candidates[index];
    	x = num/9;
    	y = num%9;
    	for i in range(1, 10):
    		board[x][y] = str(i);
    		if(self.isValid(x, y, board)):
    			if(self.sudokuSolver(board, candidates, index+1, length)):
    				return True;
    			else:
    				board[x][y] = '.';
    		else:
    			board[x][y] = '.';
    	return False;
    
    def isValid(self, x, y, board):
    	occupied = [];
    	for i in range(0, 9):
    		occupied.append(False);
    	for i in range(0, 9):
    		if(board[x][i] != '.'):
    			t = ord(board[x][i]) - ord('1');
    		else:
    			continue;
    		
    		if(occupied[t]):
    			return False;
    		else:
    			occupied[t] = True;
    			
    	for i in range(0, 9):
    		occupied[i] = False;
    	for i in range(0, 9):
    		if(board[i][y] != '.'):
    			t = ord(board[i][y]) - ord('1');
    		else:
    			continue;
    		
    		if(occupied[t]):
    			return False;
    		else:
    			occupied[t] = True;
    			
    	for i in range(0, 9):
    		occupied[i] = False;
    	dx = x/3;
    	dy = y/3;
    	for i in range(dx*3, (dx+1)*3):
    		for j in range(dy*3, (dy+1)*3):
    			if(board[i][j] != '.'):
    				t = ord(board[i][j]) - ord('1');
    			else:
    				continue;
    			
    			if(occupied[t]):
    				return False;
    			else:
    				occupied[t] = True;
    	return True;
    	
slt = Solution();
board = [['5','3','.','.','7','.','.','.','.'],
		 ['6','.','.','1','9','5','.','.','.'],
		 ['.','9','8','.','.','.','.','6','.'],
		 ['8','.','.','.','6','.','.','.','3'],
		 ['4','.','.','8','.','3','.','.','1'],
		 ['7','.','.','.','2','.','.','.','6'],
		 ['.','6','.','.','.','.','2','8','.'],
		 ['.','.','.','4','1','9','.','.','5'],
		 ['.','.','.','.','8','.','.','7','9'],
		];
slt.solveSudoku(board);
for item in board:
	print(item);