# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        curr = None
        while(list1!=None and list2!=None):
            if(list1.val <= list2.val):
                if head == None:
                    head = list1
                    curr = head
                    list1 = list1.next
                else:
                    temp = list1
                    curr.next = temp
                    curr = curr.next
                    list1 = list1.next
            else:
                if head == None:
                    head = list2
                    curr = head
                    list2 = list2.next
                else:
                    temp = list2
                    curr.next = temp
                    curr = curr.next
                    list2 = list2.next
        
        if list1 == None:
            while(list2 != None):
                if head != None:
                    curr.next = list2
                    curr = curr.next
                    list2 = list2.next
                else:
                    temp = list2
                    head = temp
                    curr = head
                    list2 = list2.next
        else:
            while(list1 != None):
                if head != None:
                    curr.next = list1
                    curr = curr.next
                    list1 = list1.next
                else:
                    temp = list1
                    head = temp
                    curr = head
                    list1 = list1.next
        
        return head