class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def __init__(self):
    	self.ans = list();
    
    def combinationSum2(self, candidates, target):
    	sol = list();
    	candidates.sort();
    	self.combinationSolver(0, candidates, target, sol);
    	return self.ans;
    
    def combinationSolver(self, start, candidates, target, sol):
    	#print(start, target, sol, self.ans);
    	if(target < 0):
    		return;
    	elif(target == 0):
    		#global ans;
    		#sol.append(candidates[start]);
    		t_sol = list(sol);
    		self.ans.append(t_sol);
    		#print("ans",self.ans);
    		return;
    	length = len(candidates);
    	for i in range(start, length):
    		if(i > start and candidates[i] == candidates[i-1]):
    			continue;
    		else:
    			sol.append(candidates[i]);
    			self.combinationSolver(i+1, candidates, target-candidates[i], sol);
    			sol.pop();
    	return;
    	
    	
    	
slt = Solution();
input_array = [10, 1, 2, 7, 6, 1, 5, 1];
print(slt.combinationSum2(input_array, 8));