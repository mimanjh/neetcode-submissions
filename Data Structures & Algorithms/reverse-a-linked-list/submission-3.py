# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = new
            new = curr
            curr = nxt

        return new