class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def power(self, base, n):
		if(n==0):
			return 1;
			
		t = self.power(base, n/2);
		if(n%2 == 0):
			res = t*t;
		else:
			res = t*t*base;
			
		return res;	
    
    def myPow(self, x, n):
    	if(n==0):
    		return 1;
    	
    	if(x==1):
    		return 1;
    	elif(x == -1):
    		if(n%2 == 0):
    			return 1;
    		else:
    			return -1;    	
    	if(n>0):
    		ans = self.power(x, n);
    	else:
    		ans = 1 / self.power(x, -n);
    	return ans;
    	

		
slt = Solution();
print(slt.myPow(0.7, 2));