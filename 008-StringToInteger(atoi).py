class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
    	str_length = len(str);
    	i = 0;
    	sign = 1;
    	ans = 0;
    	hasSign = False;
    	isValid = False;
    	INT_MAX = 2147483647;
    	INT_MIN = -2147483648;
    	while(i < str_length):
    		if(str[i] == ' '):
    			if(not isValid):
    				i = i+1;
    				continue;
    			else:
    				break;
    		elif(str[i] == '+'):
    			if(not hasSign):
    				hasSign = True;
    				isValid = True;
    				i = i+1;
    				continue;
    			else:
    				return 0;
    		elif(str[i] == '-'):
    			if(not hasSign):
    				hasSign = True;
    				isValid = True;
    				i = i+1;
    				sign = -1;
    			else:
    				return 0;
    		elif(str[i] <='9' and str[i]>='0'):
    			t =int(str[i])-int('0');
    			ans = ans*10 + t;
    			i = i+1;
    			isValid = True;
    		else:
    			break;
    			
    	ans = sign * ans;
    	if(ans > INT_MAX):
    		return INT_MAX;
    	elif(ans < INT_MIN):
    		return INT_MIN;
    	else:
    		return ans;

slt = Solution();
print(slt.myAtoi("  -+0012a42"));