# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(0)
        dummy.next = head

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow
        prev = None

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        ptr1 = prev
        ptr2 = dummy.next

        while ptr1:
            if ptr1.val != ptr2.val:
                return False
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return True

        
        