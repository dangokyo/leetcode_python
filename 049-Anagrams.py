class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
    	mymap = {};  #map(int key, list(string));
    	ans = [];
    	length = len(strs);
    	for i in range(0, length):
    		key = self.hash(strs[i]);
    		if(mymap.has_key(key)):
    			mymap[key].append(strs[i]);
    		else:
    			mymap[key] = list();
    			mymap[key].append(strs[i]);
    	for key in mymap.keys():
    		t_list = mymap[key];
    		if(len(t_list) > 1):
    			for item in t_list:
    				ans.append(item);
    		else:
    			continue;
    				
    	return ans;
    	
    def hash(self, string):
    	ans = 0;
    	length = len(string);
    	l = list();
    	for i in range(0, 26):
    		l.append(0);
    	
    	for i in range(0, length):
    		l[ord(string[i])-97] = l[ord(string[i])-97] + 1;
    	
    	for i in range(0, 26):
    		ans = ans*29 + l[i];
    	return ans; 
    
strs = ["tin","ram","zip","cry","pus","jon","zip","pyx"];
slt = Solution();
print(slt.anagrams(strs));
print(slt.hash("ida"));
print(slt.hash("diaz"));