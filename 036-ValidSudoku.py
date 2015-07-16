class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
    	occupied = [False, False, False, False, False, False, False, False, False];
    	
    	for i in range(0, 9):
    		self.nullify(occupied);
    		for j in range(0, 9):
    			if(board[i][j] == '.'):
    				continue;
    			else:
    				t = ord(board[i][j]) - ord('1');
    				if(occupied[t]):
    					#print("step 1", i, j);
    					return False;
    				else:
    					occupied[t] = True;
    					
    	for j in range(0, 9):
    		self.nullify(occupied);
    		for i in range(0, 9):
    			if(board[i][j] == '.'):
    				continue;
    			else:
    				t = ord(board[i][j]) - ord('1');
    				if(occupied[t]):
    					#print("step 2", i, j);
    					return False;
    				else:
    					occupied[t] = True;
    	
    	for i in range(0, 3):
    		for k in range(0, 3):
    			self.nullify(occupied);
    			for m in range(i*3, (i+1)*3):
    				for n in range(k*3, (k+1)*3):
    					if(board[m][n] == '.'):
    						continue;
    					else:
    						t = ord(board[m][n]) - ord('1');
    						if(occupied[t]):
    							#print("step 3", i, k, m, n);
    							return False;
    						else:
    							occupied[t] = True;
    						
    		
    	return True;
    	
    def nullify(self, vec):
    	for i in range(0, 9):
    		vec[i] = False;
    	
slt = Solution();
board = [['5','3','.','.','7','.','.','.','.'],
		 ['6','.','.','1','9','5','.','.','.'], 
		 ['.','9','8','.','.','.','.','6','.'],
		 ['8','.','.','.','6','.','.','.','3'],
		 ['4','.','.','8','.','3','.','.','1'],
		 ['7','.','.','.','2','.','.','.','6'],
		 ['.','6','.','.','.','.','2','8','.'],
		 ['.','.','.','4','1','9','.','.','5'],
		 ['.','.','.','.','8','.','.','7','9']];
print(slt.isValidSudoku(board));