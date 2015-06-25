class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
		length = len(s);
		ans = 0;
		ans_str = "";
		if(length<=1):
			return s;
		for i in range(0, length-1):
			# **a**
			left = i;
			right = i;
			#print("processing:"+str(i));
			while(left-1>=0 and right+1<length):
				if(s[left-1] == s[right+1]):
					left = left-1;
					right = right+1;
				else:
					break;
			if(right-left+1 > ans):
				#print(left, right);
				ans = right - left + 1;
				ans_str = s[left: right+1];
					
			# **aa**
			left = i;
			right = i+1;
			if(s[left] != s[right]):
				continue;
			
			while(left-1>=0 and right+1<length):
				if(s[left-1] == s[right+1] ):
					left = left-1;
					right = right +1;
				else:
					break;
			if(right - left + 1> ans):
				#print(left, right);
				ans = right - left +1 ;
				ans_str = s[left:right+1]
				
			
		return ans_str;



slt = Solution();
input_string = "acdaadf";
print(slt.longestPalindrome(input_string));
