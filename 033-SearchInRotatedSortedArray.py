class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
    	length = len(nums);
    	ans = self.searchSolver(nums, target, 0, length-1);
    	return ans;
    	
    def searchSolver(self, nums, target, left, right):
    	if(left == right):
    		if(nums[left] == target):
    			return left;
    		else:
    			return -1;
    	middle = (left + right)/2;
    	pivot = nums[middle];
    	if(pivot == target):
    		return middle;
    	if(pivot >= nums[left] and pivot <= nums[right]):
    		if(target <= pivot):
    			return self.searchSolver(nums, target, left, middle);
    		else:
    			return self.searchSolver(nums, target, middle+1, right);
    	elif(pivot <= nums[left] and pivot <= nums[right]):
    		if(target <= nums[right] and target >= pivot):
    			return self.searchSolver(nums, target, middle+1, right);
    		else:
    			return self.searchSolver(nums, target, left, middle);
    	elif(pivot >= nums[left] and pivot >= nums[right]):
    		if(target <=pivot and target >= nums[left]):
    			return self.searchSolver(nums, target, left, middle);
    		else:
    			return self.searchSolver(nums, target, middle+1, right);   		
    	


input_array = [5, 1, 3];
slt = Solution();
target = 1;
print(slt.search(input_array, target));