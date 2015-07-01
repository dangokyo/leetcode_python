class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
    	mydict = dict();
    	ans= [];
    	length = len(digits);
    	if(length==0):
    		return ans;
    	mydict['2'] = ['a','b','c'];
    	mydict['3'] = ['d','e','f'];
    	mydict['4'] = ['g','h','i'];
    	mydict['5'] = ['j','k','l'];
    	mydict['6'] = ['m','n','o'];
    	mydict['7'] = ['p','q','r','s'];
    	mydict['8'] = ['t','u','v'];
    	mydict['9'] = ['w','x','y','z'];
    	tmpsol = "";
    	self.CombinationSolver(0, tmpsol, ans, mydict, digits);
    	return ans;
    	
    def CombinationSolver(self, index, sol, ans, mydict, digits):
    	if(index == len(digits)):
    		ans.append(sol);
    		sol = sol[:-1];
    		return;
    	
    	tmp_array = mydict[digits[index]];
    	for item in tmp_array:
    		sol = sol+item;
    		self.CombinationSolver(index+1, sol, ans, mydict, digits);
    		sol = sol[:-1];
    	return;

slt = Solution();
print(slt.letterCombinations(""));