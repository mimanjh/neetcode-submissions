# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def getLength(node: ListNode):
            l = node

            counter = 0
            while l:
                counter += 1
                l = l.next
            return counter
        
        m = getLength(headA)
        n = getLength(headB)

        l1 = headA
        l2 = headB

        if m < n:
            m, n = n, m
            l1, l2 = l2, l1
        
        while m - n:
            m -= 1
            l1 = l1.next
        
        while l1 != l2:
            l1 = l1.next
            l2 = l2.next
        
        return l1
        
