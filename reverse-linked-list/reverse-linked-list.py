# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        prev = None
        curr = head
        nextNode = head.next
        
        while nextNode:
            curr.next = prev
            prev = curr
            curr = nextNode
            nextNode = curr.next
        curr.next = prev
            
        return curr