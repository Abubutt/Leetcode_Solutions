# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        decimalValue = 0
        exp = 0
        prev = None
        curr = head

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        while prev:
            decimalValue += (prev.val * (2**exp))
            prev = prev.next
            exp += 1

        return decimalValue

        