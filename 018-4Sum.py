class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
    	length = len(nums);
    	ans = [];
    	nums.sort();
    	i = length-1;
    	while(i>2):
    		t = target - nums[i];
    		t_ans = self.threeSum(nums[: i-length], t);
    		#print(nums[i], t_ans);
    		
    		for item in t_ans:
    			item.append(nums[i]);
    			ans.append(item);
    			
    		i = i-1;
    		while(nums[i] == nums[i+1] and i>0):
    			i = i-1;
    	return ans;
    	
    	
    
    def threeSum(self, nums, t):
    	ans = [];
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
    		target = t - nums[i];
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

target = 0;
input_set = [];
input_set.append(0);
input_set.append(0);
input_set.append(0);
input_set.append(0);
#input_set.append(-2);
#input_set.append(2);
slt = Solution();
print(slt.fourSum(input_set, target));