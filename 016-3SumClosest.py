class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
    	nums.sort();
    	length = len(nums);
    	MAX_INT = 2147483647;
    	ans = MAX_INT;
    	i = 0;
    	while(i < length-2):
    		left = i+1;
    		right = length-1;
    		while(left < right):
    			sum = nums[i] + nums[left] + nums[right];
    			diff = sum - target;
    			if(diff < 0):
    				left = left + 1;	
    			elif(diff > 0):
    				right = right - 1;
    			elif(diff == 0):
    				return target;
    				
    			if(abs(diff) < abs(ans - target)):
    				ans = sum;
    		i =i+1;
    	return ans;
    				
    			
    				
    			
    
input_array = [];
input_array.append(-1);
input_array.append(2);
input_array.append(1);
input_array.append(-4);

slt = Solution();
print(slt.threeSumClosest(input_array, 1));