# Understand:
# Example 1 (just one node):
#     3

# min-depth = 1 (3)

# Example 2 (one subtree is shorter, this is already given in the problem):
#     3
#    / \
#   9  20
#     /  \
#    15   7

# min-depth = 2 (3->9)

# Example 1 (a degenerate tree):
#     3
#      \
#      20
#       \
#       7

# min-depth = 3 (3->20->7)

# Plan:
# You can use DFS and output the minimum depth or use BFS which is better on average

def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    if head == None:
        return None

    dummyHead = ListNode(-1)
    dummyHead.next = head
    left = right = dummyHead

    for i in range(0, n + 1):
        right = right.next

    while right != None:
        left = left.next
        right = right.next

    left.next = left.next.next
    
    return dummyHead.next