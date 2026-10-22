# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        short, fast = head, head
        if not head:
            return False
        while short and short.next:
            fast = fast.next
            short = short.next.next
            if short and short.val == fast.val:
                return True
        return False