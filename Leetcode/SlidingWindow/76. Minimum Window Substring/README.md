## 76. Minimum Window Substring
🔗  Link: [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/description/)<br>
💡 Difficulty: Hard<br>
🛠️ Topics: String, Sliding Window, Hashtable<br>

=======================================================================================<br>
Given two strings `s` and `t` of lengths `m` and `n` respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

The testcases will be generated such that the answer is unique.

 
Example 1:<br>
Input: s = "ADOBECODEBANC", t = "ABC"<br>
Output: "BANC"<br>
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.<br>


Example 2:<br>
Input: s = "a", t = "a"<br>
Output: "a"<br>
Explanation: The entire string s is the minimum window.<br>

Example 3:<br>
Input: s = "a", t = "aa"<br>
Output: ""<br>
Explanation: Both 'a's from t must be included in the window.<br>
Since the largest window of s only has one 'a', return empty string.<br>


Constraints:<br>
m == s.length<br>
n == t.length<br>
1 <= m, n <= 10^5<br>
=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input be empty?
    - No
2. Any requirement on time/space complexity?
3. Are the characters case-sensitive? For example, is 'a' different from 'A'?
    - s and t consist of uppercase and lowercase English letters
4. Is it possible s2 is longer than s1?
    - Yes, return `""` in this case

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. Sliding Window<br>
In this problem, the sliding window technique is used to explore and iterate through substrings of string `s`. The window expands and contracts as it moves through the string, allowing efficient exploration of different candidate substrings.


2. HashMap<br>
The algorithm uses frequency dictionaries (`t_dict` and `s_dict`) to keep track of the occurrence of characters in both the target string `t` and the current window. This manipulation of character frequencies is essential for identifying valid windows.


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea:  Using a sliding window technique with two pointers (`left` and `right`) to iteratively expand and contract the window. The frequency of characters in both strings is tracked using dictionaries (`t_dict` for string t and `s_dict` for the current window in string s).

1) Initialize the length of string `s` and an empty string `ans` to store the minimum window

2) Create dictionaries `t_dict` and `s_dict` to store the frequency of characters in strings `t` and the current window of string `s`, respectively

3) Populate the `t_dict` with the frequency of characters in string `t`

4) Initialize two pointers (`left` and `right`) to track the sliding window and a counter (`required_chars`) to keep track of the characters in `t` that are still needed in the current window

5) Iterate through the characters of string `s` using the right pointer (`right`) to expand the window

6) Check if the character at the right pointer is in `t_dict`
    - If yes, update `s_dict` and decrement the `required_chars` counter

7) While all required characters from `t` are present in the current window, contract the window by moving the left pointer (`left`)    
- Update the answer if the current window is smaller than the previous minimum window

8) Move the right pointer to expand the window further

9) Repeat steps 6-8 until the right pointer reaches the end of string `s`

10) Return the minimum window stored in the variable `ans`


see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume `N` is the length of string `s`.

- Time Complexity: O(N)
- Space Complexity: O(N)