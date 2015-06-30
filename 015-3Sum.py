class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
    	ans = [];
    	nums.sort();
    	length = len(nums);
    	if(length <= 2):
    		return ans;
    		
    	i = 0;
    	while(i < length-2):
    		if(i>=1 and nums[i] == nums[i-1]):
    			i = i+1;
    			continue;
    		
    		left = i+1;
    		right = length-1;
    		target = 0 - nums[i];
    		while(left < right):
    			if(nums[left] + nums[right] > target):
    				right = right - 1;
    			elif(nums[left] + nums[right] < target):
    				left = left + 1;
    			elif(nums[left] + nums[right] == target):
    				t_ans = [];
    				t_ans.append(nums[i])
    				t_ans.append(nums[left]);
    				t_ans.append(nums[right]);
    				ans.append(t_ans);
    				left = left + 1;
    				right = right -1;
    				
    				while(left < right and nums[left] == nums[left-1]):
    					left = left + 1;
    					
    				while(left < right and nums[right] == nums[right+1]):
    					right = right - 1;
    		
    		i = i+1;
    	return ans;
    	
input_array = [];
input_array.append(-1);
input_array.append(-1);
input_array.append(0);
input_array.append(1);
input_array.append(1);
input_array.append(2);
input_array.append(2);
input_array.append(-1);
input_array.append(-4);
input_array.sort();
slt = Solution();
print(slt.threeSum(input_array));