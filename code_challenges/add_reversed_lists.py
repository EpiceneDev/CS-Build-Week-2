# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
# Input is 
    # two lists of node objects
    # nodes are listed in reverse order, both lists
    # each node is a single digit
# Add the two numbers
    # make a ListNode of each new number
    # store in the new list
# Return a linked list made of nodes with new values

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
       
        ret = curr = ListNode(0)

        while l1 or l2 or carry:
            v1 = v2 = 0

            if l1:
                v1 = l1.val
                l1 = l1.next

            if l2:
                v2 = l2.val
                l2 = l2.next

            total = v1 + v2 + carry
            # carry = total // 10
            # val = total % 10
            carry, val = divmod(total, 10)
            print(divmod(total, 10))
            curr.next = ListNode(val)
            curr = curr.next

        return ret.next
