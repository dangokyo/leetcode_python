class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
    	ans=[-1, -1];
    	length = len(nums);
    	left=searchLeft(nums, target, 0, length-1);
    	right=searchRight(nums, target, 0, length-1);
    	ans[0] = left;
    	ans[1] = right;
    	return ans;	
	
def searchLeft(nums, target, left, right):
	#print(left, right, target);
	if(left == right):
   		if(nums[left] == target):
   			return left;
   		else:
   			return -1;   				
   	middle = (left + right)/2;
   	pivot = nums[middle];
   	if(pivot >= target):
   		return searchLeft(nums, target, left, middle);
   	else:
   		return searchLeft(nums, target, middle+1, right);

def searchRight(nums, target, left, right):
	#print(left, right, target);
   	if(left == right):
   		if(nums[left] == target):
   			return left;
   		else:
   			return -1;
   	middle = (left + right)/2;
   	pivot = nums[middle+1];
   	if(pivot <= target):
   		return searchRight(nums, target, middle+1, right);
   	else:
   		return searchRight(nums, target, left, middle);


input_array = [8, 8, 10];
target = 10;
slt = Solution();
print(slt.searchRange(input_array, target));