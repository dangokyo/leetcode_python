# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
		
	def mergeTwoLists(self,l1, l2):
		ans = ListNode(0);
		cur = ans;
		t1 = l1;
		t2 = l2;
		
		while(t1 != None and t2 != None):
			if(t1.val <= t2.val):
				cur.next = t1;
				cur = t1;
				t1 = t1.next;
			else:
				cur.next = t2;
				cur = t2;
				t2 = t2.next;
				
		if(t1 != None):
			cur.next = t1;
		elif(t2 != None):
			cur.next = t2;
		return ans.next;
    	
	def mergeLists(self, left, right, lists):
		if(left == right):
			return lists[left];
		elif(left == right - 1):
			ans = self.mergeTwoLists(lists[left], lists[right]);
			return ans;
		else:
			p1 = self.mergeLists(left, (left + right)/2, lists);
			p2 = self.mergeLists((left+ right)/2+1, right, lists);
			ans = self.mergeTwoLists(p1, p2);
			return ans;
		
	def mergeKLists(self, lists):
		length = len(lists);
		if(length == 0):
			return None;
		elif(length == 1):
			return lists[0];    		
		return self.mergeLists(0, length-1, lists);
		
	

slt = Solution();
l1 = ListNode(1);
l2 = ListNode(4);
l3 = ListNode(7);
l1.next = l2; 
l2.next = l3;
l4 = ListNode(2);
l5 = ListNode(5);
l6 = ListNode(8);
l10 = ListNode(10);
l4.next = l5;
l5.next = l6;
l6.next = l10;
l7 = ListNode(3);
l8 = ListNode(6);
l9 = ListNode(9);
l7.next = l8;
l8.next = l9;
input_array = [l1, l4, l7];
t = slt.mergeKLists(input_array);
while(t!= None):
	print(t.val);
	t = t.next;
		