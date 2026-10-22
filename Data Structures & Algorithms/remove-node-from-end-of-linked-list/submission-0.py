# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1, b1 = head, None
        while p1:
            tmp1 = p1.next
            p1.next = b1
            b1 = p1
            p1 = tmp1
        p1 = b1

        rem = b1
        n2 = n
        b2 = None
        while rem and n > 1:
            b2 = rem
            rem = rem.next

            n-=1
        if b2:
            b2.next = rem.next
            rem.next = None
        else:
            p1 = p1.next

        p2 = p1
        b2 = None
        while p2:
            tmp2 = p2.next
            p2.next = b2
            b2 = p2
            p2 = tmp2
        return b2
            