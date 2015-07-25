class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        dp = [];
        length = len(nums);
        end = 0;
        for i in range(0, length):
        	dp.append(0);
        
        for i in range(0, length-1):
        	distance = nums[i];
        	print(dp);
        	if(i + distance <= end):
        		continue;
        	
        	for j in range(i+1, i+distance+1):
        		if(j >=length):
        			break;
        		
        		if(dp[j] == 0):
        			dp[j] = dp[i] + 1;
        			if(end < j):
        				end = j;
        		elif(dp[j] > 0):
        			if(dp[i] + 1 < dp[j]):
        				dp[j] = dp[i] + 1;
        			else:
        				continue;
        return dp[length-1];
        
slt = Solution();
nums = [2, 3, 1, 1, 4];
nums = [2, 1];
print(slt.jump(nums));