class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
    	ans = -1;
    	strlen = len(haystack);
    	srclen = len(needle);
    	if(srclen == 0):
    		return 0;
    	if(strlen < srclen):
    		return -1;
    	
    	for i in range(0, strlen-srclen+1):
    		if(haystack[i] == needle[0]):
    			for t in range(0, srclen):
    				if(needle[t] == haystack[i + t]):
    					if(t == srclen-1):
    						return i;
    					continue;
    				else:
    					break;
    		else:
    			continue
    	return ans;
    	
haystack = "mississippi";
needle = "issip";
slt = Solution();
print(slt.strStr(haystack, needle));