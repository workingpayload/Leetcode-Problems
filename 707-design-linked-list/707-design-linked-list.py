class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None
        

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = LinkedList(None)
        
    def __get(self, index: int) -> int:
        if index == -1:
            return self.head
        
        travel = self.head.next
        idx = 0
        
        while travel and idx < index:
            idx += 1
            travel = travel.next
            
        return None if idx != index else travel
    
    def __add_next(self, node: LinkedList, val: int) -> None:
        if node:
            self.size += 1
            curr_next = node.next
            node.next = LinkedList(val)
            node.next.next = curr_next

    def get(self, index: int) -> int:
        node = self.__get(index)
        return -1 if not node else node.val
        
    def addAtHead(self, val: int) -> None:
        node = self.head
        self.__add_next(node, val)

    def addAtTail(self, val: int) -> None:
        node = self.__get(self.size - 1)
        self.__add_next(node, val)

    def addAtIndex(self, index: int, val: int) -> None:
        node = self.__get(index - 1)
        self.__add_next(node, val)

    def deleteAtIndex(self, index: int) -> None:
        node = self.__get(index - 1)
        
        if not node or not node.next:
            return
        
        self.size -= 1
        curr_next = node.next
        node.next = curr_next.next
        curr_next = None