class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
		ans = "";
		length = len(s);
		if(numRows == 1):
			return s;
		for i in range(0, numRows):
			if(i==0):
				j = 0;
				while(j < length):
					ans = ans + s[j];
					j = j + 2*numRows -2;
			elif(i<=numRows-2 and i >=1):
				j = i;
				diff = 2*numRows - 2*(i+1);
				while(j < length):
					ans = ans + s[j];
					if(j + diff < length):
						ans = ans + s[j+diff];
					j = j + 2*numRows -2;
			elif(i==numRows-1):
				j = numRows-1;
				while(j < length):
					ans = ans + s[j];
					j = j + 2*numRows -2;
					
		return ans;
		
		
slt = Solution();
input_string = "A";
n = 1;
print(slt.convert(input_string, n));