## 21. Merge Two Sorted Lists
🔗  Link: [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/description/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: Linked List, Recursion<br>

=======================================================================================<br>
You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.


Example 1:<br>
Input: list1 = [1,2,4], list2 = [1,3,4]<br>
Output: [1,1,2,3,4,4]<br>

Example 2:<br>
Input: list1 = [], list2 = []<br>
Output: []<br>

Example 3:<br>
Input: list1 = [], list2 = [0]<br>
Output: [0]<br>

Constraints:<br>
- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in **non-decreasing** order.

=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input be empty? (head is null?)
    - Yes
2. Any requirement on time/space complexity?
    - O(m+n) in time and O(1) in space 
3. Does the linked list have a cycle?
    - No
4. Can the input lists have differing lengths?
    - Yes. Do not assume they will have the same length

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

For Linked List problems, we want to consider the following approaches:
- Multiple Pass. If we were able to take multiple passes of the linked list, would that help solve the problem?
This may help us determine the length of the list. However we do not need the length of the list
- Dummy Head. Would using a dummy head as a starting point help simplify our code and handle edge cases?
A dummy head can help us rearrange our list
- **Two Pointer**. If we used two pointers to iterate through the list at different speeds, would that help us solve this problem? 
Two pointers could help us in this problem. Where should both pointers point to initially?

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Start with a dummy head. The dummy head's next will be whichever is the smaller head of the two linked lists. Iterate through this step until one of the list's head next is null. At which point we point it to the rest of the other list

1) Instantiate a new node with a value of 0. 
   This will be our dummy node, the node to the left of the head of our return list. 
   Store a reference to this node so that we can return the list at the end.
2) Create a pointer, tail, that always points to the end of our LL. Initialize it to point to the dummy node.
3) Iterate over the LLs (while head1 or head2) where head1 and head2 are pointers to the heads of the input LLs
    1) If head1.val <= head2.val, append head1 to the list by pointing tail's next pointer to head1.
       Move head1 forward one node.
    2) Otherwise, append head2 to the list by pointing tail's next pointer to head2.
       Move head2 forward one node
4) Move tail forward one node 
5) Figure out if either list still hasn't been fully traversed.
   If it hasn't, point tail's next to the head of the list that hasn't been fully traversed.
6) Return dummy.next


### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the number of nodes in the linked list 1. M represents the number of nodes in the linked list 2.

- Time Complexity: O(N + M)
- Space Complexity: O(1), because only need to store the dummyNode as our head pointer and tail as our tail pointer.
