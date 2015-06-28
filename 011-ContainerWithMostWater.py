class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
    	length = len(height);
    	left = 0;
    	right = length-1;
    	ans = 0;
    	while(left < right):
    		t_height = min(height[left], height[right]);
    		t_ans = t_height * (right - left);
    		if(t_ans > ans):
    			ans = t_ans;
    			
    		if(height[left] <= height[right]):
    			left = left + 1;
    		else:
    			right = right - 1;
    	
    	return ans;
    
    
slt = Solution();
arr = [1, 3, 4, 5, 3, 1];
print(slt.maxArea(arr));