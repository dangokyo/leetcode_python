# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
    	tmp = head;
    	length = 0;
    	while(tmp != None):
    		length = length+1;
    		tmp = tmp.next;
    	
    	target = length - n;
    	if(target == 0):
    		return head.next;
    	
    	tmp = head;
    	t = 0;
    	while(True):
    		t = t+1;
    		if(t == target):
    			break;
    		
    		tmp = tmp.next;
    	tmp.next = tmp.next.next;	
    	return head;
    	
    
    
slt = Solution();
l1 = ListNode(1);
l2 = ListNode(2);
l3 = ListNode(3);
l4 = ListNode(4);
l5 = ListNode(5);
l1.next = l2;
l2.next = l3;
l3.next = l4;
l4.next = l5;
tmp = slt.removeNthFromEnd(l1, 5);
while(tmp!= None):
	print(tmp.val);
	tmp = tmp.next;