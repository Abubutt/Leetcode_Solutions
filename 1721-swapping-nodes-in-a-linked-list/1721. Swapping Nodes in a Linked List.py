# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        prevStart = dummy
        prevEnd = dummy
        startNode = dummy.next
        endNode = dummy.next

        slow = dummy.next
        fast = dummy.next

        for i in range(k-1):
            prevStart = prevStart.next
            fast = fast.next
        
        startNode = fast
        
        while fast and fast.next:
            prevEnd = prevEnd.next
            slow = slow.next
            fast = fast.next

        endNode = slow

        if startNode.next == endNode:
            endNext = endNode.next
            prevStart.next = endNode
            startNode.next = endNext
            endNode.next = startNode
        elif endNode.next == startNode:
            prevEnd.next = startNode
            endNode.next = startNode.next
            startNode.next = endNode
        else:
            startNext = startNode.next
            endNext = endNode.next

            prevStart.next = endNode
            endNode.next = startNext

            prevEnd.next = startNode
            startNode.next = endNext

        return dummy.next
        