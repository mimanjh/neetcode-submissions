# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursion

        # base case
        if not head or not head.next:
            return head

        # recursive call
        new_list = self.reverseList(head.next)

        # update next.next
        head.next.next = head
        # set next to None
        head.next = None

        # return new recursive list
        return new_list

# 1     ->      2       ->      3
# 1|2           2|3             3|None
# 1|None        2|1             3|2