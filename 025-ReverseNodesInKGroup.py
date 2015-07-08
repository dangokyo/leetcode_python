class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
    	ans = ListNode(0);
    	ans.next = head;
    	cur_head = ans;
    	while(cur_head != None):
    		#print(cur_head.val);
    		l_tail = self.getKthNode(cur_head, k);
    		if(l_tail == None):
    			break;
    		
    		l_head = cur_head.next;
    		counter = 1;
    		while(counter < k):
    			t_head = cur_head.next;
    			cur_head.next = l_head.next;
    			l_head.next = l_head.next.next;
    			#print(cur_head.next.val);
    			cur_head.next.next = t_head;
    			
    			counter = counter + 1;
    	
    		cur_head = l_head;
    	
    		
    	return ans.next;
    
    
    def getKthNode(self, l, k):
    	counter = 0;
    	if(l == None):
    		return None;
    	p = l;
    	while(counter < k and p!=None):
    		p = p.next;
    		counter = counter + 1;
    	
    	return p;
    		
    
    
    
l1 = ListNode(1);
l2 = ListNode(2);
l3 = ListNode(3);
l4 = ListNode(4);
l5 = ListNode(5);
l6 = ListNode(6);
l7 = ListNode(7);
l8 = ListNode(8);
l1.next = l2;
l2.next = l3;
l3.next = l4;
l4.next = l5;
l5.next = l6;
l6.next = l7;
l7.next = l8;
slt = Solution();
l = slt.reverseKGroup(l1, 5);
while(l != None):
	print(l.val);
	l = l.next;