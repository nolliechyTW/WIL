# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# iteratively
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None
        while node:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        return prev

# recursively
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head, None)
        
    def reverse(self, curr: Optional[ListNode], prev: Optional[ListNode]) -> Optional[ListNode]:
        if not curr:
            return prev
        
        nextOne = curr.next
        curr.next = prev
        
        return self.reverse(nextOne, curr)

