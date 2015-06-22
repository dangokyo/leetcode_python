class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
	ans = [];
	tmp = list(nums);
	tmp.sort();
	left = 0;
	right = len(nums)-1;
	while(left < right):
		t = tmp[left]+tmp[right];
		if(t == target):
			break;
		elif(t < target):
			left = left+1;
		else:
			right = right-1;
	for i in range(0, len(nums)):
		if(nums[i] == tmp[left]):
			ans.append(i+1);
		elif(nums[i] == tmp[right]):
			ans.append(i+1);
	return ans;

slt=Solution();
input = [3,2, 4];
target = 6
print(slt.twoSum(input, target));
