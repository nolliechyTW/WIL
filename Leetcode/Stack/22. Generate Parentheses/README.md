## 22. Generate Parentheses
🔗  Link: [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: String, Stack<br>

=======================================================================================<br>
Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:<br>
Input: n = 3<br>
Output: ["((()))","(()())","(())()","()(())","()()()"]<br>

Example 2:<br>
Input: n = 1<br>
Output: ["()"]<br>

Constraints:<br>
- 1 <= n <= 8<br>


=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1) When you mention "combinations," does that mean we need to generate all possible valid combinations, or are there specific criteria for what constitutes a valid combination?
2) Can we assume that the input n will always be a non-negative integer?
3) If n = 2, can you provide an example of the expected output? This will help clarify what is meant by "combinations of well-formed parentheses


### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Stack <br>
Stack is useful here to help keep track of the current parenthesis sequence being formed<br>

2. Backtracking<br>
Backtracking approach ensures that all valid combinations of parentheses are systematically generated<br>


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: 
1) Initialization:
- Create an empty list `res` to store valid parenthesis combinations
- Create an empty stack `stack` to keep track of the current parenthesis sequence being formed

2) **Define Backtracking Function (backtrack)**:
- Define a recursive function backtrack that takes counts of open and close parentheses as parameters
    - Base Case:
        - If counts of open and close parentheses both equal n, add the current combination in the stack to the result list (res)
        - Return to backtrack and explore other possibilities
    - Recursive Steps:
        - Try adding an opening parenthesis `(` if the count of open parentheses is less than n
        - Append an opening parenthesis to the stack
        - Recursively call backtrack with an incremented count of open parentheses `(open+1)`
        - **Pop the last character from the stack to backtrack and explore other possibilities**
        - Try adding a closing parenthesis `)` if the count of close parentheses is less than the count of open parentheses
        - Append a closing parenthesis to the stack
        - Recursively call backtrack with an incremented count of close parentheses (close+1)
        - **Pop the last character from the stack to backtrack and explore other possibilities**
3) Start Backtracking:
    - Invoke the backtrack function with initial counts of open and close parentheses set to 0
4) Return Result:
    - Return the list of valid parenthesis combinations

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

<!-- Assume N be the total number of elements in array tokens.

- Time Complexity: O(N)
- Space Complexity: O(N) -->
