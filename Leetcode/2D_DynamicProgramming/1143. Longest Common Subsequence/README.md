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
- `text1` and `text2` consist of only lowercase English characters.

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


- Dymanic Programming <br>
Dealing with an optimization problem, we usually use either DP or greedy algorithm to solve it. The best way of doing this is by drawing an example and playing around with it. Here we go with DP.<br>
Recall that there are two different techniques we can use to implement a dynamic programming solution; *memoization* and *tabulation*.<br>
- **Memoization** is where we add caching to a function (that has no side effects). In dynamic programming, it is typically used on **recursive** functions for a **top-down** solution that starts with the initial problem and then recursively calls itself to solve smaller problems.
- **Tabulation** uses a table to keep track of subproblem results and works in a **bottom-up** manner: solving the smallest subproblems before the large ones, in an iterative manner. Often, people use the words "tabulation" and "dynamic programming" interchangeably.


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: implements a 2D dynamic programming approach to construct a 2D grid to store intermediate results, updating the grid based on character matches and maximizing the subsequence length at each step.

1. Grid Initialization: A grid `dp` is created, slightly larger than the sizes of `text1` and `text2`. It's filled with zeros to track the length of the common subsequence at different points.

2. Iterating Through Strings: goes through each character of `text1` and `text2`. It compares characters from both strings to find matches.

3. Updating the Grid: When matching characters are found, the grid is updated to reflect the longer subsequence. If characters don't match, the code chooses the longer subsequence found so far.

4. Result: The final value in the grid represents the length of the longest common subsequence for the entire strings. 

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume `N` represents the length of `text1` and `M` represents the length of `text2`.


- Time Complexity: O(N * M)
- Space Complexity: O(N * M)
