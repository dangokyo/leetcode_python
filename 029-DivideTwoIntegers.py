class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
    	t1 = abs(dividend);
    	t2 = abs(divisor);
    	sign = 1;
    	INT_MAX = 2147483647;
    	if(dividend == 0):
    		return 0;
    	
    	if(dividend < 0):
    		sign = sign *(-1);
    		
    	if(divisor < 0):
    		sign = sign *(-1);
    		
    	ans = 0;
    	while(t1 >= t2):
    		t = t2;
    		t_ans = 1;
    		shift = 0;
    		while(True):
    			if(t1 < t):
    				t = t >> 1;
    				t_ans = t_ans << (shift-1);
    				#print(t_ans);
    				ans = ans + t_ans;
    				break;
    			elif(t1 >= t):
    				shift = shift + 1;
    				t = t << 1;
    				
    		t1 = t1 - t;
    	if(ans > INT_MAX and sign > 0):
    		return INT_MAX;
    	else:
    		return ans*sign;

slt = Solution();
print(slt.divide(21, 3));