# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
    	ans = ListNode(0);
    	ans.next = head;
    	
    	cur = ans;
    	p = head;
    	
    	while(True):
    		if(p == None):
    			break;
    		elif(p.next == None):
    			break;
    			
    		cur.next = p.next;
    		p.next = cur.next.next;
    		cur.next.next = p;
    		
    		cur = p;
    		p = p.next;
    	
    	
    	
    	return ans.next;
    
l1 = ListNode(1);
l2 = ListNode(2);
l3 = ListNode(3);
l4 = ListNode(4);
#l1.next = l2;
#l2.next = l3;
#l3.next = l4;
slt = Solution();
l = slt.swapPairs(l1);
while(l != None):
	print(l.val);
	l = l.next;