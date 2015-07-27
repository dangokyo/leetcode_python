class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def __init__(self):
    	self.ans = list();
    	self.numbers = list();
    	self.visited = list();
    	self.length = 0;
    	
    def permuteUnique(self, nums):
    	sol = list();
    	nums.sort();
    	self.numbers = nums;
    	#print(self.numbers);
    	self.length = len(nums);
    	for i in range(0, self.length):
    		self.visited.append(False);
    	
    	self.permuteSolver(sol);
    	return self.ans;
    	
    
    def permuteSolver(self, sol):
    	#print(sol);
    	length = len(sol);
    	#print(length, self.length);
    	if(length == self.length):
    		t = list(sol);
    		self.ans.append(t);
    		return;
    	i=0;	
    	while(i < self.length):
    		if self.visited[i]:
    			i = i+1
    			continue;
    		else:
    			sol.append(self.numbers[i]);
    			self.visited[i] = True;
    			self.permuteSolver(sol);
    			sol.pop();
    			self.visited[i] = False;
    			i = i+1;
    			while(i < self.length and self.numbers[i] == self.numbers[i-1]):
    				i = i+1;

slt = Solution();
numbers = [1, 1, 3];
print(slt.permuteUnique(numbers));