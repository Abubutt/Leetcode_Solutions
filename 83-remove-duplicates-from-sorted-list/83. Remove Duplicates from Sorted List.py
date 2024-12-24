# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        leftPtr = head
        rightPtr = head.next
        
        while rightPtr:
            if leftPtr.val == rightPtr.val:
                leftPtr.next = rightPtr.next
                rightPtr = rightPtr.next
            else:
                leftPtr = leftPtr.next
                rightPtr = rightPtr.next
                
        return head
            
        