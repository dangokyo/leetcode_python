class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
    	length = len(s);
    	i = 0;
    	ans = 0;
    	mydict = dict();
    	mydict['I'] = 1;
    	mydict['V'] = 5;
    	mydict['X'] = 10;
    	mydict['L'] = 50;
    	mydict['C'] = 100;
    	mydict['D'] = 500;
    	mydict['M'] = 1000;
    	while(i<length-1):
    		if(mydict[s[i+1]] <= mydict[s[i]] ):
    			ans = ans + mydict[s[i]];
    		else:
    			ans = ans - mydict[s[i]];
    		i = i+1;
    	ans = ans + mydict[s[length-1]];
    	return ans;
    
    
slt = Solution();
input_string = "LXXXIX";
print(slt.romanToInt(input_string));