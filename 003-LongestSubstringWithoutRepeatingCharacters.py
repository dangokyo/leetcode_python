class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
	mydict = dict();
	length = len(s);

	if(length == 0):
		return 0;
	elif(length == 1):
		return 1;
	
	left = 0;
	right = 0;
	ans = 0;
	mydict[s[0]] = 0;
	while(right < length):
		right = right + 1;
		if(right >= length):
			right = right-1;
			break;

		t = s[right];
		if t in mydict.keys():
			t_index = mydict[t];
			if(t_index < left):
				mydict[t] = right;
			else:
				mydict[t] = right;
				left = t_index+1;
		else:
			mydict[t] = right;
		#print(right, left);
		if(right - left + 1 > ans):
			ans = right - left + 1;


	if(right - left + 1> ans):
		ans = right - left + 1;

	return ans;

slt = Solution();
input_string = "aa";
print(slt.lengthOfLongestSubstring(input_string));
