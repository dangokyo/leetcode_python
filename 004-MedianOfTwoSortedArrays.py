class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}

	def findMedianSortedArrays(self, nums1, nums2):
		length1 = len(nums1);
		length2 = len(nums2);
		if(length1 == 0 and length2 != 0):
			ans = self.getMedian(nums2);
		elif(length1 != 0 and length2 == 0):
			ans = self.getMedian(nums1);
		elif(length1 == 0 and length2 == 0):
			ans = 0;
		else:
			ans = self.getMedianSortedArray(nums1, nums2);
		return ans;

	def getMedianSortedArray(self, nums1, nums2):
		length1 = len(nums1);
		length2 = len(nums2);

		t = length1 + length2;
		if(t%2 == 1):
			ans = self.MedianSortedArraySolver(0, length1-1, 0, length2-1, nums1, nums2, (t/2+1));
		else:
			t1 = self.MedianSortedArraySolver(0, length1-1, 0, length2-1, nums1, nums2, t/2+1);
			t2 = self.MedianSortedArraySolver(0, length1-1, 0, length2-1, nums1, nums2, t/2);
			ans = float(t1+t2)/2;
		return ans;

	#get the kth number from the nums1[left1: right1] and nums2[left2: right2]: 1, 2, 3, 4, 5, 6, 7....nth
	def MedianSortedArraySolver(self, left1, right1, left2, right2, nums1, nums2, k):
		#print(left1, right1, left2, right2, k);
		if(k==1):
			return min(nums1[left1], nums2[left2]);
		if(left1 == right1 and left2 == right2):
			if(k == 2):
				return max(nums1[left1], nums2[left2]);
			elif(k==1):
				return min(nums1[left1], nums2[left2]);
		elif(left1 == right1 and left2 < right2):
			if(nums1[left1] > nums2[left2 + k -1]):
				return nums2[left2 + k -1];
			else:
				return max(nums1[left1], nums2[left2+k-2]);
		elif(left2 == right2 and left1 < right1):
			if(nums2[left2] > nums1[left1+k-1]):
				return nums1[left1+k-1];
			else:
				return max(nums2[left2], nums1[left1+k-2]);
		else:
			mid1 = (left1 + right1)/2;
			mid2 = (left2 + right2)/2;
			leftpart = mid1 - left1 + 1 + mid2 - left2 + 1;
			if(leftpart >= k + 1):
				if(nums1[mid1] >= nums2[mid2]):
					return self.MedianSortedArraySolver(left1, mid1, left2, right2, nums1, nums2, k);
				else:
					return self.MedianSortedArraySolver(left1, right1, left2, mid2, nums1, nums2, k);
			else:
				if(nums1[mid1] >= nums2[mid2]):
					return self.MedianSortedArraySolver(left1, right1, mid2+1, right2, nums1, nums2, k-(mid2-left2+1));
				else:
					return self.MedianSortedArraySolver(mid1+1, right1, left2, right2, nums1, nums2, k-(mid1-left1+1));
				

	def getMedian(self, nums):
		length = len(nums);
		if(length%2 == 1):
			return nums[length/2];
		else:
			return float(nums[length/2] + nums[length/2 - 1]) / 2; 


	

in1 = [1, 2, 3, 4, 5, 8, 9, 10, 12, 14];
in2 = [3, 5, 7, 8, 10];
in3 = [];
slt = Solution();

print(slt.findMedianSortedArrays(in1, in2));

