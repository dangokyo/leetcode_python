class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
    	if(x<0):
    		return False;
    		
    	tmp = x;
    	ans = 0;
    	while(tmp > 0):
    		ans = ans*10 + (tmp%10);
    		tmp = tmp/10;
    	
    	return (ans == x);

slt = Solution();
print(slt.isPalindrome(1234321));