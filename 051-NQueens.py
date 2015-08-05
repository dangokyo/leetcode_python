class Solution:
    # @param {integer} n
    # @return {string[][]}
    def solveNQueens(self, n):
    	sol = list();
    	ans = list();
    	if(n==1):
    		sol.append("Q");
    		ans.append(list(sol));
    		return ans;
    	
    	row = '.' * n;
    	for i in range(0, n):
    		sol.append(list(row));
    	
    	#for i in range(0, n):
    	#	sol[1][i] = 'Q';
    	
    	self.NQueenSolver(ans, sol, 0, n);
    	return ans;
    
    def NQueenSolver(self, ans, sol, level, n):
    	if(level == n):
    		res = list();
    		for item in sol:
    			res.append(''.join(item));
    		ans.append(res);
    		return;
    	
    	row = level;
    	for col in range(0, n):
    		sol[row][col] = 'Q';
    		if(self.isValid(sol, row, col, n)):
    			self.NQueenSolver(ans, sol, level+1, n);
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
    	



slt = Solution();
n = 4;
result = slt.solveNQueens(n);
for item in result:
	for line in item:
		print(line);
	print("");