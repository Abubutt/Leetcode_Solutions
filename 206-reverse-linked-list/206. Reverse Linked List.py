# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head, prevNode):
            if head == None:
                return prevNode

            nextNode = head.next
            head.next = prevNode
            prevNode = head
            head = nextNode

            return reverse(head, prevNode)

        return reverse(head, None)
        