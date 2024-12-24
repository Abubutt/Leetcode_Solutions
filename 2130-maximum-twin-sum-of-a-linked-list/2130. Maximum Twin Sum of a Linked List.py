# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dummy1 = head
        slow = head
        fast = head

        maxTwinSum = 0
        length = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            length+=1

        curr = slow
        prev = None

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        dummy2 = prev

        for i in range(length):
            maxTwinSum = max(maxTwinSum, dummy1.val + dummy2.val)
            dummy1 = dummy1.next
            dummy2 = dummy2.next
        
        return maxTwinSum




        
        