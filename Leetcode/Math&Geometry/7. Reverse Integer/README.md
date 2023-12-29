## 7. Reverse Integer
🔗  Link: [Reverse Integer](https://leetcode.com/problems/reverse-integer/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Math<br>

=======================================================================================<br>

Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-231, 231 - 1]`, then return `0`.

*Assume the environment does not allow you to store 64-bit integers (signed or unsigned).*

Example 1:<br>
Input: x = 123<br>
Output: 321<br>


Example 2:<br>
Input: x = -123<br>
Output: -321<br>

Example 3:<br>
Input: x = 120<br>
Output: 21<br>


Constraints:<br>
- -2^31 <= x <= 2^31 - 1

=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input integer be 0?
- ofc! 
2. How should the function handle invalid inputs, such as non-integer values?
- we can ignore this situation
3. Are there any time or space complexity constraints I should be aware of?
- an optimal solution would have O(n) in both time and space complexity
### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. String<br>
The core task requires transforming the input integer into a format that allows character-by-character manipulation. Once we have the integer as a string, we can apply string manipulation techniques. The key operation here is reversing the string. After manipulating the string, the final step is to convert the reversed string back into an integer. <br>

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Directly manipulate the string representation of the integer.

1) Converts the absolute value of the integer to a string.
2) Reverses the string.
3) Converts the reversed string back to an integer.
4) Applies the sign based on the original integer's sign.
5) Checks for 32-bit integer overflow, returning 0 if it occurs.
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N is the number of digits in the input integer.

- Time Complexity: O(N)
- Space Complexity: O(N)
