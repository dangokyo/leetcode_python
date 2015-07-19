class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
		ans = "";
		if(n == 1): 
			return "1";	
		sol = self.countAndSay(n-1);
		cur = sol[0];
		length = len(sol);
		count = 1;
		ans = "";
		for i in range(1, length):
			if(sol[i] == cur):
				count = count + 1;
			else:
				ans = ans + str(count)+ cur;
				cur = sol[i];
				count = 1;
				#print(ans);
		ans = ans + str(count)+ cur;
		return ans;
    
slt = Solution();
n = 7;
print(slt.countAndSay(n));