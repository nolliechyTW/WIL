# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy head. This will be our reference to our return list + Create a curr pointer that helps us build the return list
        dummyNode = curr = ListNode()
        
        # Initialize a variable to store the carry value, if any, as we compute the sum. 
        carry = 0
        
        # Traverse the two lists while our two pointers is not null and carry is not 0.
        while l1 or l2 or carry:
            
            # Find the values at each pointer
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            
            # Find and store their sum
            total = num1 + num2 + carry
            singleDigitTotal = total % 10
            
            # Calculate the carry over value, if any
            carry = total // 10 
            
            # Create and attach a new node with summed value to the return list
            curr.next = ListNode(singleDigitTotal)
            
            # Repeat with next nodes
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        # Return dummy.next
        return dummyNode.next
