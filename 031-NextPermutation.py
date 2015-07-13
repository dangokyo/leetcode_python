class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
    	length = len(nums);
    	if(length <= 1):
    		return;
    	
    	i = length - 2;
    	while(i >= 0):
    		cur_max = 2147483647;
    		cur_pos = 0;
    		for k in range(i+1, length):
    			if(nums[k] > nums[i] and nums[k] < cur_max):
    				cur_pos = k;
    				cur_max = nums[k];
    		#print(i, cur_pos);
    		if(cur_pos > 0):
    			t = nums[cur_pos];
    			nums[cur_pos] = nums[i];
    			nums[i] = t;
    			nums[i+1:length+1] = sorted(nums[i+1:length+1]);
    			return
    		
    		i = i - 1;
    	if(i < 0):
    		nums.sort();
    		return;
    		
slt = Solution();
input_array = [1, 3, 4, 2];
slt.nextPermutation(input_array);
print(input_array);