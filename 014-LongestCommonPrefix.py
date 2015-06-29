class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
    	size = len(strs);
    	ans = "";
    	if(size == 0):
    		return ans;
    	elif(size == 1):
    		return strs[0];
    		
    	tStr = strs[0];
    	sLength = len(tStr);
    	i = 0;
    	Flag = True;
    	while(i < sLength and Flag):
    		t = tStr[i];
    		for k in range(1, size):
    			if(i >= len(strs[k])):
    				Flag = False;
    				break;
    			if(t != strs[k][i]):
    				Flag = False;
    				break;
    		if(Flag):	
    			ans = ans+t;
    	
    		i = i+1;
    	return ans;
    
slt = Solution();
input_array = [];
input_array.append("stuio");
#input_array.append("studion");
#input_array.append("station");
print(slt.longestCommonPrefix(input_array));