# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        else:
            next_node = head.next
            curr = head
            prev = None
            while(next_node != None):
                curr.next = prev
                prev = curr
                curr = next_node
                next_node = next_node.next
            curr.next = prev
            return curr

