# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        dummy = head
        ct = 0

        while dummy:
            ct += 1
            dummy = dummy.next

        if k % ct == 0:
            return head
        
        slow = head
        fast = head

        tail = None
        prev = None

        for i in range(k % ct):
            tail = fast
            fast = fast.next

        while fast:
            prev = slow
            slow = slow.next
            tail = fast
            fast = fast.next

        prev.next = None
        tail.next = head

        head = slow

        return head
        