# Last updated: 5/4/2025, 2:15:14 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        slow, fast = head, head

        while head:
            if fast == None:
                return slow
            if fast.next == None:
                return slow
            slow = slow.next
            fast = fast.next.next
            head = head.next
