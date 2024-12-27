class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.total = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.total:
            return -1

        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode
        
        if self.total == 0:  # was empty
            self.tail = newNode
        
        self.total += 1

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        if self.total == 0:  # was empty
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        
        self.total += 1

    def addAtIndex(self, index: int, val: int) -> None:
        # If index > total, do nothing (by typical problem statement convention)
        if index < 0 or index > self.total:
            return
        
        if index == 0:
            self.addAtHead(val)
        elif index == self.total:
            self.addAtTail(val)
        else:
            # Insert somewhere in the middle
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            newNode = ListNode(val)
            newNode.next = prev.next
            prev.next = newNode
            self.total += 1

    def deleteAtIndex(self, index: int) -> None:
        # If index >= total or index < 0, do nothing
        if index < 0 or index >= self.total:
            return

        if index == 0:
            # Delete the head
            self.head = self.head.next
            self.total -= 1
            # If list is now empty, tail should be None
            if self.total == 0:
                self.tail = None
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            
            # node to delete
            nodeToDelete = prev.next
            prev.next = nodeToDelete.next
            self.total -= 1
            # If we deleted the old tail, update self.tail
            if index == self.total:  
                # that means we removed the last node
                self.tail = prev
