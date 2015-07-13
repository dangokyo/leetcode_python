class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
    	ans = 0;
    	length = len(s);
    	mystack = [];
    	for i in range(0, length):
    		if(s[i] == '('):
    			mystack.append(i);
    		elif(s[i] == ')'):
    			if(len(mystack)!= 0 and s[mystack[-1]] == '('):
    				#print(mystack[-1]);
    				mystack.pop();
    				if(len(mystack) == 0):
    					sol = i+1;
    				else:
    					sol = i-mystack[-1];
    				ans = max(sol, ans);
    			else:
    				mystack.append(i);
    	return ans;
    	
    	
input_string = ")()())";
slt = Solution();
print(slt.longestValidParentheses(input_string));