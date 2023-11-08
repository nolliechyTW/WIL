## 125. Valid Palindrome
🔗  Link: [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/description/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: Two Pointers, String<br>

=======================================================================================<br>
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

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
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Constraints:<br>
1 <= s.length <= 2 * 10^5<br>
s consists only of printable ASCII characters.
=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input string be empty? 
    - Yes, and the result should be `true`
2. Any requirement on time/space complexity? 
    - Solve in O(1) space complexity
3. Does removing all non-alphanumeric characters means only ASCII character should be consindered?
    - Yes


### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. Left and Right Pointers <br>
We can create two pointers: one starts from the left and the other starts from the right. When left pointer and right pointer pointing at different valid character, we exit and return false immediately. This can ensure that we don't need extra space.


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Start traversing inwards, from both ends of the input string, and we can expect to see the same characters, in the same order

1) Initialize two pointer variables, left and right, and point them to the two ends of the input string
2) Move the left pointer to the right until it points to an alphanumeric character. Similarly, move the right pointer to the left until it also points to an alphanumeric character
3) Check the characters pointed to by left and right:
    - If they are not alphanumeric, move pointers accordingly
    - If the characters are different (after converting them to lowercase), return False
    - If the characters are the same, continue checking the next characters
4) After the loop finishes, which means right exceeds left, the string is considered a palindrome. Therefore, return True

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the number of characters in the string.


- Time Complexity: O(N)
- Space Complexity: O(1)
