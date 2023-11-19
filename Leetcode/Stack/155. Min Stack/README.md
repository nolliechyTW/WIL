## 155. Min Stack
🔗  Link: [Valid Parentheses](https://leetcode.com/problems/min-stack/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Design, Stack<br>

=======================================================================================<br>
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:
- `MinStack()` initializes the stack object
- `void push(int val)` pushes the element val onto the stack
- `void pop()` removes the element on the top of the stack
- `int top()` gets the top element of the stack
- `int getMin()` retrieves the minimum element in the stack


Example 1:<br>
Input:<br>
["MinStack","push","push","push","getMin","pop","top","getMin"]<br>
[[],[-2],[0],[-3],[],[],[],[]]<br>

Output:<br>
[null,null,null,null,-3,null,0,-2]<br>

Explanation:
MinStack minStack = new MinStack();<br>
minStack.push(-2);<br>
minStack.push(0);<br>
minStack.push(-3);<br>
minStack.getMin(); // return -3<br>
minStack.pop();<br>
minStack.top();    // return 0<br>
minStack.getMin(); // return -2<br>


Constraints:<br>
- -2^31 <= val <= 2^31 - 1
- Methods pop, top and getMin operations will always be called on non-empty stacks.
- At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1) Should we account for calling pop(), top(), or getMin() on an empty MinStack?
    - We can assume these functions will always be called on non-empty stacks.
2) Should pop() also return the top element of the MinStack?
    - No. In this case, pop only removes the top element and does not return anything.
3)  Besides implementing a common stack structure it is important to consider how we might update the new minimum after popping off the old so that we can easily return the newly updated minimum value in constant time
4) Any requirement on time/space complexity?
    - You must implement a solution with O(1) time complexity for each function


### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Stack <br>
Stack is useful here since we can easily keep track of the last bracket. We also want to match with the LATEST brackets was recorded when a closing bracket is identified.

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: 
1) have two stacks
    - One stack keeps track of all the number
    - The other(minStack) only keeps track of min numbers
        - When adding a value, if the value is currently smaller than the top of minStack, then also add new value to minStack
2) Pseudocode
    - Create 2 stack in our constructor when the minStack class is instantiated
        - push(int val)
            - push value to stack1
            - if the val < current min, push it to stack2 also
        - getMin() 
            - if stack2 is empty, return max integer
            - else return stack2.peek()
        - pop()
            - return top element of stack1
            - if that element is the min, also remove from stack2
        - top()
            - stack1.peek()

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N be the total number of operations performed.


- Time Complexity: O(1)
- Space Complexity: O(N)
