## 125. Valid Palindrome
🔗  Link: [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/description/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: String, Two Pointers<br>

=======================================================================================<br>

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.<br>

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.


Example 1:<br>
Input: s = "A man, a plan, a canal: Panama"<br>
Output: true<br>
Explanation: "amanaplanacanalpanama" is a palindrome.<br>


Example 2:<br>
Input: s = "race a car"<br>
Output: false<br>
Explanation: "raceacar" is not a palindrome.<br>

Example 3:<br>
Input: s = " "<br>
Output: true<br>
Explanation: s is an empty string "" after removing non-alphanumeric characters.<br>
Since an empty string reads the same forward and backward, it is a palindrome.<br>

Constraints:<br>
- 1 <= s.length <= 2 * 10^5

=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1.  Any requirement on time/space complexity?
- O(n) in time complexity and O(1) in space complexity
2. Can you confirm the range of characters that the input string might contain? Are we considering just ASCII characters, or should the solution also handle Unicode characters (which might include emojis, symbols, etc.)?
- `s` consists only of printable ASCII characters.
3. Are there any specific edge cases you'd like the solution to handle? For example, empty strings, strings with only one character, or strings with only non-alphanumeric characters?
- you should handle all of them 

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


- Two pointers<br>
Since we got a hint that this question should be solved in O(1) space complexity, instead of using string manipulation or array to brute force the problem, we can simply use two pointers to neglect characters that are not valid. This approach allows us to evaluate the palindrome property in place, without the need for additional data structures.

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: With two pointers, one at the beginning and one at the end of the string, we can compare the characters these pointers refer to. If both characters are alphanumeric and identical (considering case insensitivity), we move the pointers closer to the center of the string, continuing this process. Whenever we encounter non-alphanumeric characters, we can skip them by moving the respective pointer inwards. This way, we efficiently ignore invalid characters and focus only on the parts of the string that matter for palindrome validation.<br>

1) Initialize Pointers
- Start with two pointers, `left` at the beginning and `right` at the end of the string.
2) Traverse String with Pointers
- Use a `while` loop to move `left` and `right` towards each other, stopping when they meet or cross.
3) Skip Non-Alphanumeric Characters
- Inside the loop, increment `left` and decrement `right` to skip over any non-alphanumeric characters.
4) Character Comparison
- Compare the characters at `left` and `right` indices, considering case insensitivity. If they don't match, return `False`.
5) Move Pointers and Repeat
- If characters match, move `left` one step right and `right` one step left, then repeat the comparison.
6) Complete Check
- If the loop completes without mismatches, return `True`, indicating the string is a palindrome.

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N is the length of the string `s`.

- Time Complexity: O(N)
- Space Complexity: O(1)