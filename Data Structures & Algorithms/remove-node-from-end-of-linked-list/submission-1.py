# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr.next:
            size+=1
            curr = curr.next
        loc = size - n
        curr = head
        while loc > 0:
            curr = curr.next
            loc -= 1
        if loc >= 0:
            curr.next = curr.next.next if curr.next else None
        else:
            head = head.next
        return head
        