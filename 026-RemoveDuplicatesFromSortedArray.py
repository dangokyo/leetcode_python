class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
    	length = len(nums);
    	if(length == 0):
    		return 0;
    		
    	pos = 0;
    	for i in range(0, length):
    		if(nums[i] != nums[pos]):
    			pos = pos+1;
    			nums[pos] = nums[i];
    		else:
    			continue;
    	return pos+1;
    
slt = Solution();
input_array = [1,1,2,3,4,4]
print(slt.removeDuplicates(input_array));
print(input_array)