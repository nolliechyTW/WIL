## 3. Longest Substring Without Repeating Characters
🔗  Link: [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, Sliding Window<br>

=======================================================================================<br>
Given a string `s`, find the length of the longest substring without repeating characters.

Example 1:<br>
Input: s = "abcabcbb"<br>
Output: 3<br>
Explanation: The answer is "abc", with the length of 3.<br>

Example 2:<br>
Input: s = "bbbbb"<br>
Output: 1<br>
Explanation: The answer is "b", with the length of 1.<br>

Constraints:<br>
- 0 <= s.length <= 5 * 10^4
- `s` consists of English letters, digits, symbols and spaces
=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input be empty?
    - No
2. Any requirement on time/space complexity?
    - O(n) time and O(1) space will do
3. Are the characters case-sensitive? For example, is 'a' different from 'A'?
    - Yes

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. Sliding Window<br>
We can maintain a set to keep track of characters in the current window and use two pointers to represent the start and end of the window. **Move the end pointer until a repeating character is found, then move the start pointer to eliminate the repeated character**. Keep track of the maximum length of the window.

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Record the max length found as we proceed through the array and keep checking whether there is repeating character in the string

1) Initialize variables `seen` to keep track of unique characters in the current substring and `left` to keep track of the length of the sliding window
2) Iterate through the characters of the input string `s` using the variable `right` as the right pointer of the sliding window 
    - Check for repeating characters
    - Update set and calculate length
3) Return result


### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the length of the string and M is the size of the character set

- Time Complexity: O(N)
- Space Complexity: O(min(M, N))
