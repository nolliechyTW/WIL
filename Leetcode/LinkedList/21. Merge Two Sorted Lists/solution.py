class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Instantiate a new node with a value of 0 + Create a pointer, tail, that always points to the end of our LL. Initialize it to point to the dummy node.
        dummyNode = tail = ListNode()
        
        # Iterate over the LLs (while head1 or head2) where head1 and head2 are pointers to the heads of the input LLs
        while list1 and list2:
            # If head1.val <= head2.val, append head1 to the list by pointing tail's next pointer to head1.
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                # Otherwise, append head2 to the list by pointing tail's next pointer to head2
                tail.next = list2
                list2 = list2.next
                
            # Move tail forward one node 
            tail = tail.next
                
        # Figure out if either list still hasn't been fully traversed. +  If it hasn't, point tail's next to the head of the list that hasn't been fully traversed.
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        
        # Return dummy.next
        return dummyNode.next