class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
    	RomanVacabulary = ['I', 'V', 'X', 'L', 'C', 'D', 'M'];
    	digit = 0;
    	ans = "";
    	while(num>0):
    		val = num%10;
    		#print(digit, val);
    		if(val <=3 and val>=1):
    			ans = RomanVacabulary[digit]*val + ans;
    		elif(val == 4):
    			ans = RomanVacabulary[digit] + RomanVacabulary[digit+1] + ans;
    		elif(val >= 5 and val <= 8):
    			ans = RomanVacabulary[digit+1] + RomanVacabulary[digit]*(val-5)+ ans;
    		elif(val == 9):
    			ans = RomanVacabulary[digit] + RomanVacabulary[digit+2] + ans;  		
    		num = num/10;
    		digit = digit + 2;
    	return ans;
    	
slt = Solution();
print(slt.intToRoman(99));