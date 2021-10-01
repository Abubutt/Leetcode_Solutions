# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tempHead = head
        size = 0
        while tempHead:
            size+=1
            tempHead = tempHead.next
        
        if size-n == 0:
            return head.next
        
        c = 0
        tempHead = head
        while tempHead:
            if c==size-n-1:
                tempHead.next = tempHead.next.next
                return head
            tempHead = tempHead.next
            c+=1
            
            