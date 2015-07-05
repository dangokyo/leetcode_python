class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
    	if(l1 == None):
    		return l2;
    	elif(l2 == None):
    		return l1;
    		
    	p1 = l1;
    	p2 = l2;
    	head = ListNode(1);
    	cur = head;
    	
    	while(p1 != None and p2 != None):
    		if(p1.val <= p2.val):
    			cur.next = p1;
    			cur = p1;
    			p1 = p1.next;
    		else:
    			cur.next = p2;
    			cur = p2;
    			p2 = p2.next;
    			
    	if(p1!=None):
    		cur.next = p1;
    	elif(p2 != None):
    		cur.next = p2;
    	
    	return head.next;
    	
    	
    	
slt = Solution();
l1 = ListNode(1);
l2 = ListNode(2);
l3 = ListNode(8);
l4 = ListNode(4);
l5 = ListNode(5);
l6 = ListNode(6);

l1.next = l2;
l2.next = l3;
l4.next = l5;
l5.next = l6;

l = slt.mergeTwoLists(l1, l4);
while(l!=None):
	print(l.val);
	l = l.next;