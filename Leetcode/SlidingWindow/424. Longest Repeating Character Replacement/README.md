## 424. Longest Repeating Character Replacement
🔗  Link: [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, Sliding Window, Hashtable<br>

=======================================================================================<br>
You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.<br>

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:<br>
Input: s = "ABAB", k = 2<br>
Output: 4<br>
Explanation: Replace the two 'A's with two 'B's or vice versa.<br>

Example 2:<br>
Input: s = "AABABBA", k = 1<br>
Output: 4<br>
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.<br>


Constraints:<br>
1 <= s.length <= 10^5
0 <= k <= s.length
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
    - s consists of only uppercase English letters

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. Sliding Window<br>
Using a sliding window is iterable and ordered and is normally used for a longest, shortest or optimal sequence that satisfies a given condition. 

2. HashMap<br>
Using a HashMap to keep track of the frequency of characters in the current window.


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: The initial step is to extend the window to its limit, that is, the longest we can get to with maximum number of modifications. We will want to change the less frequent characters to the most frequent characters in the substring. As we progress, the sliding window technique will play a crucial role in dynamically adjusting the position of the `left` variable. This ensures that we consistently capture the optimal segment.

1) Initialize Variables:
- Create an empty dictionary `frequencyMap` to store the frequency of characters in the current window
- Initialize a variable `res` to 0, which will store the length of the longest valid substring
- Initialize `left` and `right` pointers to the start of the string

2) Iterate Over the String:
Use a `for` loop to iterate over each character in the string `s` using the `right` pointer.

3) Update Frequency Map:
- Update the frequency of the current character in the frequencyMap.

4) **Check Validity of Window**:
- Use a while loop to check if the current window is valid. The condition `(right - left + 1) - max(frequencyMap.values()) > k ` checks whether the window size minus the frequency of the most frequent character is greater than k.
- If it is not valid, shrink the window by moving the left pointer one step to the right and update the frequency map accordingly.

5) Update Result:
Update the result res with the maximum length encountered so far (right - left + 1).

6) Return Result


### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the number of characters in the given string and M is the size of the number of uppercase English letters, which is actually 26.

- Time Complexity: O(N)
- Space Complexity: O(1)