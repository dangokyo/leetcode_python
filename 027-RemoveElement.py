class Solution:
	# @param {integer[]} nums
    # @param {integer} val
	# @return {integer}
	def removeElement(self, nums, val):
		length = len(nums);
		pos = 0;
		for i in range(0, length):
			if(nums[i]!=val):
				nums[pos] = nums[i];
				pos = pos + 1;
		return pos

slt = Solution();
input_array = [1,1,2,3,4,4];
print(slt.removeElement(input_array, 1));
print(input_array);