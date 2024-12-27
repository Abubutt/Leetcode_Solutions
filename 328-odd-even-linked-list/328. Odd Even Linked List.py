# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummyOdd = ListNode(0)
        dummyOdd.next = head

        dummyEven = ListNode(0)
        dummyEven.next = head.next

        curr1 = head
        curr2 = head.next

        while curr2 and curr2.next:
            curr1.next = curr1.next.next
            curr2.next = curr2.next.next

            curr1 = curr1.next
            curr2 = curr2.next

        curr1.next = dummyEven.next

        return dummyOdd.next

        