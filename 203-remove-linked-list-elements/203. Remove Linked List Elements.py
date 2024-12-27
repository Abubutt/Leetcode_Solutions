# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            nextNode = curr.next
            if curr.val == val:
                prev.next = nextNode
                curr.next = None
            else:
                prev = prev.next
            curr = nextNode

        return dummy.next


        