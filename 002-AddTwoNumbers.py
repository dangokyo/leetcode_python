# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x;
		self.next = None;

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
	carry = 0;
	if(l1==None and l2 == None):
		return None;
	elif(l1==None and l2 != None):
		return l2;
	elif(l1!=None and l2 == None):
		return l1;

	p1 = ListNode;
	p2 = ListNode;
	ans = ListNode(0);
	p = ans;
	p1 = l1;
	p2 = l2;
	while(p1!=None or p2!= None):
		if(p1!= None):
			t1 = p1.val;
			p1 = p1.next;
		else:
			t1 = 0;

		if(p2!= None):
			t2 = p2.val;		
			p2 = p2.next;
		else:
			t2 = 0;

		t = t1 + t2 + carry;
		carry = t/10;
		t = t%10;
		#print("test:"+str(t));
		p.next = ListNode(t);
		p = p.next;
	if(carry != 0):
		p.next = ListNode(carry);	
	return ans.next;


t1=ListNode(2);
t2=ListNode(4);
t3=ListNode(3);
t8=ListNode(4);
t4=ListNode(5);
t5=ListNode(6);
t6=ListNode(4);
t7=ListNode(8);
t1.next = t2;
t2.next = t3;
t3.next = t8;
t4.next = t5;
t5.next = t6;
t6.next = t7;
slt = Solution();
t = slt.addTwoNumbers(t1, t4);
while(t!=None):
	print(t.val);
	t = t.next;
