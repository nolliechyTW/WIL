## 150. Evaluate Reverse Polish Notation
🔗  Link: [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, Stack<br>

=======================================================================================<br>
You are given an array of strings `tokens` that represents an arithmetic expression in a [Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation).

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
- The valid operators are '+', '-', '*', and '/'.
- Each operand may be an integer or another expression.
- The division between two integers always truncates toward zero.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in a 32-bit integer.

Example 1:<br>
Input: tokens = ["2","1","+","3","*"]<br>
Output: 9<br>
Explanation: ((2 + 1) * 3) = 9<br>

Example 2:<br>
Input: tokens = ["4","13","5","/","+"]<br>
Output: 6<br>
Explanation: (4 + (13 / 5)) = 6<br>

Example 3:<br>
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]<br>
Output: 22<br>
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5<br>
= ((10 * (6 / (12 * -11))) + 17) + 5<br>
= ((10 * (6 / -132)) + 17) + 5<br>
= ((10 * 0) + 17) + 5<br>
= (0 + 17) + 5<br>
= 17 + 5<br>
= 22<br>


Constraints:<br>
- 1 <= tokens.length <= 10^4<br>
- tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200]


=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1) Can we assume that the 'tokens' array will always contain at least one element?
    - Yes
2) Any requirement on time/space complexity?
    - O(n) in time and O(n) in space


### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Stack <br>
Stack is useful here if we learned postfix before!! This is exactly the same implementation.

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: 
1) Initialize an empty stack to keep track of operands during the evaluation.
2) Iterate through each token in the input 'tokens' array.
3) For each token:
    - If it is an operand (not one of the operators '+', '-', '*', '/'), convert it to an integer and push it onto the stack.
    - If it is an operator, pop the top two elements from the stack. Perform the corresponding operation based on the operator and push the result back onto the stack.
4) After processing all tokens, the final result should be on the top of the stack. Pop it and return as the final result.

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N be the total number of elements in array tokens.

- Time Complexity: O(N)
- Space Complexity: O(N)
