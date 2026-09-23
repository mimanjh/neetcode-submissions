class ListNode:
    def __init__(self, val = 0):
        self.val = val
        self.next = None

class MyStack:

    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, x: int) -> None:
        node = ListNode(x)
        curr = self.head

        node.next = curr
        self.head = node

        self.size += 1

    def pop(self) -> int:
        res = curr = self.head
        
        self.head = curr.next
        if self.size > 1:
            self.next = curr.next.next
        else:
            self.next = None

        self.size -= 1
        return res.val

    def top(self) -> int:
        return self.head.val

    def empty(self) -> bool:
        return self.size == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()