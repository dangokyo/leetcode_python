class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
    	ans = [];
    	word_number = len(words);
    	if(word_number == 0):
    		return ans;
    	word_length = len(words[0]);
    	string_length = len(s);
    	if(string_length == 0):
    		return ans;
    	if(string_length < word_number * word_length):
    		return ans;
    	
    	expectCount = {};
    	for item in words:
    		if(expectCount.has_key(item)):
    			expectCount[item] = expectCount[item]+1;
    		else:
    			expectCount[item] = 1;
    	#for item in expectCount.keys():
    	#	print(item + str(expectCount[item]))	
    	mywords = {};
    	for i in range(0, string_length - word_length+1):
    		sub = s[i:i+word_length];
    		if(expectCount.has_key(sub)):
    			mywords[i] = sub;
    		else:
    			mywords[i] = "";
    	#print(mywords);
    	for i in range(0, word_length):
    	
    		k = i;
    		realCount = {};
    		count = 0;
    		#print(k);
    		start = i;
    		while(k <= string_length - word_length):
    			t = mywords[k];
    			#print(start, k, t);
    			if(t == ""):
    				realCount = {};
    				count = 0;
    				start = k + word_length;
    				k = k+word_length;
    				continue;
    			else:
    				if(realCount.has_key(t)):
    					realCount[t] = realCount[t]+1;
    					count = count + 1;
    				else:
    					realCount[t] = 1;
    					count = count + 1;
    			#print(t, count,k, realCount[t], expectCount[t]);	
    			if(realCount[t] > expectCount[t]):
					while(mywords[start] != t):
						realCount[mywords[start]] = realCount[mywords[start]] - 1;
						start = start + word_length;
						count = count -1;
					realCount[t] = realCount[t] - 1;
					start = start + word_length;
					count = count - 1;
    			
    			
    			k = k+word_length;
    			
    			if(count == word_number):
    				ans.append(start);
    	
    	return ans;

slt = Solution();
s = "cbarfoothefoobarman";
words = ["foo", "bar"];
print(slt.findSubstring(s,words));