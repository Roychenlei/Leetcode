#!/user/bin/env python
#coding: 'utf-8'

class ListNode(object):
	def __init__(self,x):
		self.val=x
		self.next=None


class Solution(object):
	def addTwoNumbers(self,l1,l2):
		ret = ListNode(0)
		cur = ret

		sum=0

		while True:
			if l1 != None:
				sum += l1.val
				l1 = l1.next
			if l2 != None:
				sum += l2.val
				l2 = l2.next

			cur.val = sum % 10
			sum /= 10
			if l1 != None or l2 != None or sum != 0:
				cur.next =ListNode(0)
				cur =cur.next
			else:
				break
		return ret


if __name__ == '__main__':
    print "----------------- start -----------------"

    l1_1 = ListNode(2)
    l1_2 = ListNode(4)
    l1_3 = ListNode(3)
    l1_1.next = l1_2
    l1_2.next = l1_3

    l2_1 = ListNode(5)
    l2_2 = ListNode(6)
    l2_3 = ListNode(4)
    l2_1.next = l2_2
    l2_2.next = l2_3

    l3_1 = Solution().addTwoNumbers(l1_1,l2_1)
    while l3_1 != None:
        print l3_1.val
        l3_1 = l3_1.next
