## 20. Valid Parentheses
🔗  Link: [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: String, Stack<br>

=======================================================================================<br>
Given a string s containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1) Open brackets must be closed by the same type of brackets
2) Open brackets must be closed in the correct order
3) Every close bracket has a corresponding open bracket of the same type



Example 1:<br>
Input: s = "()"<br>
Output: true<br>

Example 2:<br>
Input: s = "()[]{}"<br>
Output: true<br>

Example 3:<br>
Input: s = "(]"<br>
Output: false<br>

Constraints:<br>
- 1 <= s.length <= 10^4<br>
- s consists of parentheses only '()[]{}'<br>
=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input string be empty?
- No
2. Can a bracket be inside a pararnthesis?
- Yes
3. Any requirement on time/space complexity?
- O(n) in time and space complexity

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Stack <br>
Stack is useful here since we can easily keep track of the last bracket. We also want to match with the LATEST brackets was recorded when a closing bracket is identified.

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Create a map to associate sorted strings (keys) with the original input strings (values). After populating the map, return the values as a list of lists.

1) create a stack to keep track of open brackets only
2) iterate through string
    - if encounter a open bracket, push it to the stack
        - if encounter a closing bracket, check against the top element of the stack
            - if the top element is not a matching closing, return false
            - else pop off the top of the stack 
3) if we reach the end of the string and the stack is empty, return true
    - else return false

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N is the length of the input string.

- Time Complexity: O(N)
- Space Complexity: O(N)
