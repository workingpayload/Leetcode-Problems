# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        
        if not lists and len(lists)==0:
            return None
        
        
        while(len(lists)>1):
            
            mergedlist = []
            
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1)<len(lists) else None
                
                mergedlist.append(self.mergetwo(l1,l2))
                
            lists = mergedlist
            
        return lists[0]    
            
    

    def mergetwo(self,l1,l2):
        
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            
            if l1.val<l2.val:
                tail.next = l1
                l1 = l1.next
                
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next    
                
                
        if l1:
            tail.next = l1
            
        if l2:
            tail.next = l2
            
        return dummy.next    
            
            
            
            
    
        