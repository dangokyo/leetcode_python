class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
    	t1 = (int)(num1);
    	t2 = (int)(num2);
    	print(t1, t2);
    	t = t1 * t2;
    	return (str)(t);
    
num1 = "1341234139481";
num2 = "2945723495820345897";
slt = Solution();
print(slt.multiply(num1, num2));