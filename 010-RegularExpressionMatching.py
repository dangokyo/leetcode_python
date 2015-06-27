class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
    	str_length = len(s);
    	pattern_length = len(p);
    	i = 0;
    	while(i+3<pattern_length):
    		if(p[i] == p[i+2] and p[i+1]== '*' and p[i+3] == '*'):
    			p = p[0:i] + p[i+2:pattern_length];
    		else:
    			i = i+1;
    		pattern_length = len(p);
    	#print(p);
    	ans = self.matchSolver(0, 0, s, p);
    	return ans;
    	
    def matchSolver(self, str_index, pattern_index, s, p):
    	#print(str_index, pattern_index);
    	if(pattern_index == len(p)):
    		if(str_index == len(s)):
    			return True;
    		else:
    			return False;
    	
    	elif(pattern_index == len(p)-1):
    		if(str_index == len(s)-1 and (p[pattern_index]=='.' or (p[pattern_index] == s[str_index]))):
    			return True;
    		else:
    			return False;
    		
    	elif(str_index == len(s)):
    		i = pattern_index;
    		while(i <= len(p)):
    			if(i == len(p)):
    				return True;
    			elif(i == len(p)-1):
    				return False;
    			
    			if(p[i+1]== '*'):
    				i = i+2;
    			else:
    				return False;
    	
    	flag1 = False;
    	flag2 = False;
    	if(p[pattern_index+1] == '*'):
    		flag1 = self.matchSolver(str_index, pattern_index+2, s, p);
    		
    		if(flag1 == True):
    			return True;
    		elif(p[pattern_index]=='.' or (p[pattern_index] == s[str_index])):
    			flag2 = self.matchSolver(str_index+1, pattern_index, s, p);
    			return flag2;
    		else:
    			return False;
    	else:
    		if(p[pattern_index]=='.' or (p[pattern_index] == s[str_index])):
    			flag2 = self.matchSolver(str_index+1, pattern_index+1, s, p);
    		else:
    			flag2 = False;
    		
    		return flag2;
    		
    	
 

slt = Solution();
#s = "aaaccbccbcbaabcaa";
#p = "c*a*.*a*.*c*.c*.a*c";
#s = "bc";
#p = ".ca*c*"
s = "aaaaaaaaaaaaaaaaab";
p = "a*a*a*a*a*a*a*a*a*b"
print(slt.isMatch(s, p));