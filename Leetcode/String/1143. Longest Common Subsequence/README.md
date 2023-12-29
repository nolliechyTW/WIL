## 1143. Longest Common Subsequence
🔗  Link: [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: String, DP<br>

=======================================================================================<br>
Given two strings `text1` and `text2`, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A *subsequence* of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
- For example, "ace" is a subsequence of "abcde". <br>
A common subsequence of two strings is a subsequence that is common to both strings.


Example 1:<br>
Input: text1 = "abcde", text2 = "ace" <br>
Output: 3  <br>
Explanation: The longest common subsequence is "ace" and its length is 3.<br>

Example 2:<br>
Input: text1 = "abc", text2 = "abc"<br>
Output: 3<br>
Explanation: The longest common subsequence is "abc" and its length is 3.<br>

Example 3:<br>
Input: text1 = "abc", text2 = "def"<br>
Output: 0<br>
Explanation: There is no such common subsequence, so the result is 0.<br>

Constraints:<br>
- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters.
=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input be empty?
2. Any requirement on time/space complexity?
3. Will the length for two inputs be different

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


- Storing the elements of the string in a Hashtable <br>
As we iterate through the string, we can store each character in a Hashtable. If the character is already in the Hashtable, then we increment its count by 1. Otherwise, we add the character to the Hashtable and set its count to 1.

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Create a hashtable to store characters and their frequencies for both strings s and t. After storing the characters from both strings, compare them element-wise and count-wise. If they are identical, return True; otherwise, return False.

1) Create Hashtable for s and t respectivley
2) Iterate through numbers
    - If number is already in Hashtable, count ++
    - Else store number in Hashtable and set its count = 1 
3) Compare two Hashtable


### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the number of items in the s and t.


- Time Complexity: O(N)
- Space Complexity: O(N)
