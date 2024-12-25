# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        slow = head
        fast = head.next

        while fast:
            if slow.val == fast.val:
                while fast and slow.val == fast.val:
                    fast = fast.next
                
                prev.next = fast
                if fast == None:
                    break
                slow = fast
                fast = fast.next
            else:
                prev = prev.next
                slow = slow.next
                fast = fast.next
        
        return dummy.next


        return dummy.next
            