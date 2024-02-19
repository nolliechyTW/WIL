## 844. Backspace String Compare
🔗  Link: [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/description/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: Two Pointers, String, Stack<br>

=======================================================================================<br>
Given two strings `s` and `t`, return `true` if they are equal when both are typed into empty text editors. `'#'` means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:<br>
Input: s = "ab#c", t = "ad#c"<br>
Output: true<br>
Explanation: Both s and t become "ac".<br>

Example 2:<br>
Input: s = "ab##", t = "c#d#"<br>
Output: true<br>
Explanation: Both s and t become "".<br>

Example 3:<br>
Input: s = "a#c", t = "b"<br>
Output: false<br>
Explanation: s becomes "c" while t becomes "b".<br>

Constraints:<br>
- 1 <= s.length, t.length <= 200
- s and t only contain lowercase letters and '#' characters
=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input string be empty? 
2. Any requirement on time/space complexity? 
- Can you solve it in `O(n)` time and **`O(1)`** space?


### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1.  Two Pointers<br>
Using two-pointers can avoid using auxiliary data structures that depend on the input size. Besides, processing backspaces naturally suggests a backward traversal from the end, as the impact of a backspace is on the characters before it. There's a need to compare, pair, or otherwise process elements from opposite ends or different parts of the data structure simultaneously.


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: iterating through both strings **from the end towards the beginning**, simulating the backspace effect as we go. This method allows us to compare characters without actually modifying the strings or using extra space to store the final results


1) Initialize Two Pointers: Start with two pointers, each pointing to the end of the two strings (`s` and `t`) respectively. These pointers will be used to traverse the strings backwards.

2) Define a Helper Function: Implement a helper function, `find_next_valid_char_index`, that takes a string and a starting index as inputs. This function will:
    - Count the number of backspace (#) characters encountered.
    - Move the index backwards, effectively skipping characters that are "erased" by backspaces.
    - Return the index of the next valid character that is not erased by a backspace, or stop if no such character exists (i.e., the start of the string is reached).

3) Iterate Backwards through Both Strings: Use a loop to simultaneously move backwards through both strings by adjusting the pointers with the help of the helper function. For each iteration:
    - Use the helper function to adjust the pointers index1 and index2 for strings `s` and `t`, respectively, to point to the next valid character that should be compared.
    - If both pointers move past the beginning of their respective strings (indicating that both strings have been fully processed), conclude that the strings are equal and return `True`.

4) Character Comparison: At each step after adjusting the pointers, perform the following checks:
    - If one pointer is less than 0 (indicating the end of one string has been reached) but the other is not, or if the characters at the current pointers do not match, return `False`, as the strings are not equal.
    - If both pointers are less than 0, return `True`, as both strings have been fully processed and are considered equal.

5) Move Pointers Backwards: If the current characters match (or both strings are at a point where comparison is valid), decrement both pointers by 1 to move to the previous characters in the strings for the next iteration.

6) Repeat the Process: Continue the iterative process of adjusting pointers, comparing characters, and moving the pointers backwards until a mismatch is found or both strings are fully compared and found to be equal.

7) Return the Result: The algorithm returns `True` if the strings are equal after considering all backspace operations, and `False` otherwise.


### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N is the length of the longer string.

- Time Complexity: O(N)
- Space Complexity: O(1)
