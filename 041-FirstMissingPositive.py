class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
		length = len(nums);
		if(length == 0):
			return 1;
		i = 0;
		end = length - 1;
		while(i < length):
			#print(nums, i);
			if(nums[i] == i+1):
				i = i + 1;
				continue;
			elif(nums[i] < 1 or nums[i] > length):
				#t = nums[i];
				#nums[i] = nums[end];
				#nums[end] = t;
				#end = end - 1;
				i = i + 1;
			else:
				if(nums[i] == nums[nums[i] - 1]):	
					#t = nums[i];
					#nums[i] = nums[end];
					#nums[end] = t;
					#end = end - 1;
					i = i+1;
				else:
					index = nums[i];
					t = nums[index - 1];
					nums[index - 1] = nums[i];
					nums[i] = t;
		#print(nums);
		for i in range(0, length):
			if(nums[i] != i + 1):
				return i+1;
		return length+1;
				#i = i -1;
			#i = i+1;
		
nums = [3, 4, -1, 1];
#nums = [0, 2, 1];
#nums = [];
slt = Solution();
print(slt.firstMissingPositive(nums));