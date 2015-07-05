class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
    	length = len(s);
    	stack = list();
    	i = 0;
    	while(i<length):
    		if(s[i]=='(' or s[i]=='[' or s[i] == '{'):
    			stack.append(s[i]);
    		elif(s[i] == ')'):
    			if(len(stack) == 0):
    				return False;
    				
    			if(stack[-1] == '('):
    				stack.pop();
    			else:
    				return False;
    		elif(s[i] == ']'):
    			if(len(stack) == 0):
    				return False;
    				
    			if(stack[-1] == '['):
    				stack.pop();
    			else:
    				return False;
    		elif(s[i] == '}'):
    			if(len(stack) == 0):
    				return False;
    				
    			if(stack[-1] == '{'):
    				stack.pop();
    			else:
    				return False;
    		i = i+1;
    	if(len(stack) == 0):
    		return True;
    	else:
    		return False;
    	
    	
input_string = "([)]";
slt = Solution();
print(slt.isValid(input_string));