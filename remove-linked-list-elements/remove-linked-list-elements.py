# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        tempHead = head
        if not head:
            return None
        while head:       # if the head value is = val
            if head.val == val:
                head = head.next
            else:
                break     # to come out of while loop
        prev = None
        temp = head
        while temp != None:
            if temp.val != val:   # just updating the temp and prev
                prev = temp
                temp = temp.next
            else:
                prev.next = temp.next   # deleting the node
                temp = temp.next 
        return head
                
            
        