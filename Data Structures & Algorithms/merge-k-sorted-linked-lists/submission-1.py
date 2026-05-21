# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)>0:
            list1 = lists[0]
            for i in range(1,len(lists)):
                list1 = self.merge2Lists(list1,lists[i])
            
            return list1
        else:
            print("I am returning empty list")
            return None
            

    def merge2Lists(self, list1, list2):
        sorted_list = None
        head = None

        while(list1 and list2):
            if list1.val <= list2.val:
                nwln = ListNode(list1.val)
                list1 = list1.next
            else:
                nwln = ListNode(list2.val)
                list2 = list2.next
            
            if sorted_list:
                sorted_list.next = nwln
                sorted_list = sorted_list.next
            else:
                head = nwln
                sorted_list = nwln
        
        if list1:
            while(list1):
                nn = ListNode(list1.val)
                sorted_list.next = nn
                sorted_list = sorted_list.next
                list1 = list1.next
        elif list2:
            while(list2):
                nn = ListNode(list2.val)
                sorted_list.next = nn
                sorted_list = sorted_list.next
                list2 = list2.next
        
        return head