# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        size = 0
        curr = head
        while(curr):
            size += 1
            curr = curr.next
        if size > 1:
            mid = size // 2
            fp = head
            bp = None
            while mid > 0:
                bp = fp
                fp = fp.next
                mid -= 1
            if bp:
                bp.next = None
            # reverse the second half of the list
            prev = None
            curr = fp
            np = fp.next
            while(np):
                curr.next = prev
                prev = curr
                curr = np
                np = np.next if np else None
            curr.next = prev

            # Reorder
            l1np = head.next
            l2np = curr
            curr = head

            while(l1np or l2np):
                curr.next = l2np
                l2np = l2np.next if l2np else None
                curr = curr.next
                curr.next = l1np
                l1np = l1np.next if l1np else None
                curr = curr.next if curr.next else curr
            
        
        