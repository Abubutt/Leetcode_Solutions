# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, list1: ListNode, list2: ListNode) -> ListNode:
        a_pointer, b_pointer = list1, list2
        while a_pointer != b_pointer:
            a_pointer = a_pointer.next if a_pointer else list2
            b_pointer = b_pointer.next if b_pointer else list1
        return a_pointer