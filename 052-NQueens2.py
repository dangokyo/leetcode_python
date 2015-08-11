class Solution:
    # @param {integer} n
    # @return {string[][]}
    def __init__(self):
    	self.ans = 0;
    
    def totalNQueens(self, n):
    	sol = list();
    	#ans = list();
    	if(n==1):
    		return 1;
    	
    	row = '.' * n;
    	for i in range(0, n):
    		sol.append(list(row));
    	
    	self.NQueenSolver(sol, 0, n);
    	return self.ans;
    
    def NQueenSolver(self, sol, level, n):
    	if(level == n):
    		self.ans = self.ans + 1;
    		return;
    	
    	row = level;
    	for col in range(0, n):
    		sol[row][col] = 'Q';
    		if(self.isValid(sol, row, col, n)):
    			self.NQueenSolver(sol, level+1, n);
    		sol[row][col] = '.';
    	return;
    	
    def isValid(self, sol, row, col, n):
    	for i in range(0, n):
    		if(i == col):
    			continue;
    		elif(sol[row][i] == 'Q'):
    			return False;
    	for i in range(0, n):
    		if(i==row):
    			continue;
    		elif(sol[i][col] == 'Q'):
    			return False;
    	i = 1;
    	while(row+i<n and col+i<n):
    		if(sol[row+i][col+i] == 'Q'):
    			return False;
    		else:
    			i = i+1;
    			
    	i = 1;
    	while(row+i<n and col-i>=0):
    		if(sol[row+i][col-i] == 'Q'):
    			return False;
    		else:
    			i = i+1;
    	i = 1;
    	while(row-i>=0 and col+i<n):
    		if(sol[row-i][col+i] == 'Q'):
    			return False;
    		else:
    			i = i+1;
    			
    	i = 1;
    	while(row-i>=0 and col-i>=0):
    		if(sol[row-i][col-i] == 'Q'):
    			return False;
    		else:
    			i = i+1;
    	return True;
    	




for n in range(1, 10):
	slt = Solution();
	print( slt.totalNQueens(n));