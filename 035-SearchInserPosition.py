class Solution:
	# @param {integer[]} nums
	# @param {integer} target
	# @return {integer}
	def searchInsert(self, nums, target):
		length = len(nums);
		if(length == 0):
			return 0;
			
		if(target <= nums[0]):
			return 0;
		if(target == nums[length-1]):
			return length-1;
		if(target > nums[length-1]):
			return length;
			
		ans = self.searchSolver(nums, target, 0, length-1);
		return ans;
		
	def searchSolver(self, nums, target, left, right):
		if(left == right):
			return left;
		elif(left + 1 == right):
			if(nums[left] == target):
				return left;
			else:
				return right;
				
		middle = (left + right)/2;
		pivot = nums[middle];
		if(pivot == target):
			return middle;
		elif(pivot > target):
			return self.searchSolver(nums, target, left, middle);
		elif(pivot < target):
			return self.searchSolver(nums, target, middle, right);
	
input_array = [1, 3, 5, 7];
target = 7;
slt = Solution();
for i in range(0, 9):
	print(slt.searchInsert(input_array, i));