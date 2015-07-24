class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
    	stringLength = len(s);
    	patternLength = len(p);
    	if(patternLength == 0):
    		return (stringLength == 0);
    	
    	stringIndex = 0;
    	patternIndex = 0;
    	preStringIndex = 0;
    	prePatternIndex = -1;
    	
    	while(stringIndex < stringLength):
    		#print(stringIndex, preStringIndex, patternIndex, prePatternIndex);
    		if(patternIndex < patternLength):
    			if(s[stringIndex] == p[patternIndex] or p[patternIndex]=='?'):
    				patternIndex = patternIndex + 1;
    				stringIndex = stringIndex + 1;
    			elif(p[patternIndex] == '*'):
    				preStringIndex = stringIndex;
    				prePatternIndex = patternIndex;
    				patternIndex = patternIndex + 1;
    			elif(prePatternIndex < 0):
    				return False;
    			elif(prePatternIndex >=0):
    				stringIndex =preStringIndex + 1;
    				preStringIndex = stringIndex;
    				patternIndex = prePatternIndex;
    		elif(prePatternIndex >=0):
    			stringIndex =preStringIndex + 1;
    			preStringIndex = stringIndex;
    			patternIndex = prePatternIndex;
    		else:
    			break;
    	
    	#print("final:", stringIndex, preStringIndex, patternIndex, prePatternIndex);
    	if(stringIndex < stringLength):
    		return False;
    	
    	while(patternIndex < patternLength):
    		if(p[patternIndex]=='*'):
    			patternIndex = patternIndex+1;
    		else:
    			break;
    			
    	if(patternIndex == patternLength):
    		return True;
    	else:
    		return False;
    
    
string = "abefcdgiescdfimde"
pattern = "ab*cd?i*de"
slt = Solution();
print(slt.isMatch(string, pattern));