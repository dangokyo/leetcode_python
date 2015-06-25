class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
    	INT_MAX = 2147483647;
    	INT_MIN = -2147483648;
    	if(x < 0):
    		sign = -1;
    	else:
    		sign = 1;
    	a = abs(x);
    	ans = 0;
    	while(a > 0):
    		t = a%10;
    		ans = ans*10 + t;
    		a = a/10;
    	ans = ans*sign;
    	
    	if(ans < INT_MIN or ans > INT_MAX):
    		return 0;	
    	
    	return ans;
    

slt = Solution();
print(slt.reverse(100000000));