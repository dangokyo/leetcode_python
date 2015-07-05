class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
		dp = dict();
		dp[0] = [];
		dp[1] = ["()"];
		if(n==0 or n==1):
			return dp[n];
			
		for i in range(2, n+1):
			tmp_set = set();
			
			print(dp[i-1]);
			for item in dp[i-1]:
				tmp_set.add('(' + item + ')');
			
			for k in range(1, i):
				for item1 in dp[k]:
					for item2 in dp[i-k]:
						tmp_set.add(item1+item2);
			dp[i] = list(tmp_set);
		
		return dp[n];
		
		
slt = Solution();
print(slt.generateParenthesis(5));    
    
    
