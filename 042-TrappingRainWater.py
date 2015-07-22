class Solution:
    # @param {integer[]} height
    # @return {integer}
    def __init__(self):
    	self.heights = list();	
    
    def trap(self, height):
    	self.heights= height;
    	length = len(height);
    	left = 0;
    	ans = 0;
    	while(left < length - 1):
    		while(left < length-1 and height[left] <= height[left+1]):
    			left = left + 1;
    		
    		right = min(length-1, left+1);
    		while(right < length):
    			if(right == length-1):
    				break;
    				
    			if(height[right] <= height[left] and height[right]< height[right+1]):
    				right = right + 1;
    			elif(height[right] <= height[left] and height[right] >= height[right+1]):
    				for i in range(right+1, length):
    					if(height[i] > height[right] and height[i] < height[left]):
    						right = i;
    					elif(height[i] > height[right] and height[i] >= height[left]):
    						right = i
    						break;
    				break;
    			elif(height[right] > height[left] and height[right] <= height[right+1]):
    				right = right + 1;
    			elif(height[right] > height[left] and height[right] > height[right+1]):
    				break; 
    		ans = ans + self.getVolumne(left, right);
    		left = right;
    	return ans;
    
    def getVolumne(self, left, right):
    	#print(left, right);
    	sol = 0;
    	h = min(self.heights[left], self.heights[right]);
    	for i in range(left, right):
    		sol = sol + max(0, h - self.heights[i]);
    	return sol;
    	
    
heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1];
heights = [5,5,1,7,1,1,5,2,7,6];
slt = Solution();
print(slt.trap(heights));