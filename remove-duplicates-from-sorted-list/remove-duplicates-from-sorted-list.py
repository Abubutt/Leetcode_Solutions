# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        curr = head
        visited = set([curr.val])
        while curr.next:
            if curr.next.val in visited:
                curr.next = curr.next.next
            else:
                visited.add(curr.next.val)
                curr = curr.next
        return head
                
                
                