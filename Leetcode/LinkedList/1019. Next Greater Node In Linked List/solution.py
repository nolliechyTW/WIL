class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # Convert the linked list to an array for easier access to elements.
        # This simplifies comparing values since linked lists don't support direct indexing.
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        # Initialize an answer array with zeros for each element in the list.
        # This array will store the next greater value for each node. If no greater value is found, it remains 0.
        ans = [0] * len(arr)
 
        # Use a stack to keep track of the indices for which we haven't found a next greater element yet.
        # The stack helps in efficiently finding the next greater element for each node.
        stack = []
        
        # Iterate through the array representation of the list
        for i, value in enumerate(arr):
            # If the stack is not empty and the current value is greater than the value at the index
            # at the top of the stack, it means we've found a next greater element for the node at stack's top.
            while stack and value > arr[stack[-1]]:
                idx = stack.pop()  # Remove the top index from the stack.
                ans[idx] = value  # Update the answer for the node at this index with the current value.
            
            # For each node, add its index to the stack. This index represents a node for which
            # we are yet to find a next greater element. As we proceed, we'll try to find a greater
            # element for these stored indices.
            stack.append(i)
        
        return ans  # Return the completed answer array, filled with next greater values for each node.
