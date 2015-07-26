class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def __init__(self):
    	self.ans = list();
    	self.numbers = list();
    	self.length = 0;
    
    def permute(self, nums):
    	sol = list();
    	self.numbers = nums;
    	self.length = len(nums);
    	self.permuteSolver(sol);
    	return self.ans;
    
    def permuteSolver(self, sol):
    	length = len(sol);
    	#print(length, self.length);
    	if(length == self.length):
    		t = list(sol);
    		self.ans.append(t);
    		return;
    		
    	for i in range(0, self.length):
    		if self.numbers[i] in sol:
    			continue;
    		else:
    			sol.append(self.numbers[i]);
    			self.permuteSolver(sol);
    			sol.pop();

slt = Solution();
numbers = [1, 2, 3];
print(slt.permute(numbers));