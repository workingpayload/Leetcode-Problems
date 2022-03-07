# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None and list2!=None:
            return list2
        elif list1!=None and list2==None:
            return list1
        elif list1==None and list2==None:
            return list1
        
        new, temp = None,None 
        
        while list1 and list2:
            if new==None:
                if list1.val<list2.val:
                    new = ListNode(list1.val)
                    list1 = list1.next
                    temp = new
                else:
                    new = ListNode(list2.val)
                    list2 = list2.next
                    temp = new
            else:
                if list1.val<list2.val:
                    temp.next = ListNode(list1.val)
                    list1 = list1.next
                    temp = temp.next
                else:
                    temp.next = ListNode(list2.val)
                    list2 = list2.next
                    temp = temp.next
                    
        if list1==None and list2!=None:
            temp.next = list2
        elif list1!=None and list2==None:
            temp.next = list1
        return new    
        