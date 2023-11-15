## 567. Permutation in String
🔗  Link: [Permutation in String](https://leetcode.com/problems/permutation-in-string/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, Sliding Window, Hashtable<br>

=======================================================================================<br>
Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of s1's permutations is the **substring** of s2.

Example 1:<br>
Input: s1 = "ab", s2 = "eidbaooo"<br>
Output: true<br>
Explanation: s2 contains one permutation of s1 ("ba").<br>

Example 2:<br>
Input: s1 = "ab", s2 = "eidboaoo"<br>
Output: false<br>

Constraints:<br>
1 <= s1.length, s2.length <= 10^4
=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input be empty?
    - No
2. Any requirement on time/space complexity?
    - O(n) time and O(m) space will do
3. Are the characters case-sensitive? For example, is 'a' different from 'A'?
    - s1 and s2 consist of lowercase English letters.
4. Is it possible s1 is shorter than s2?
    - Yes

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. Sliding Window<br>
Using a sliding window to check if any permutation of s1 is present in s2 by maintaining a moving window and updating character frequencies as the window slides through the input string

2. HashMap<br>
Using a HashMap to keep track of the frequency of characters in the current window.


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea:  Using a sliding window technique and maintaining a character frequency dictionary to efficiently track the occurrences of characters within the sliding window.


1) Initialization:
- Initialize a dictionary (char_freq) to store the frequency of characters in the sliding window.
- Set the window size (window_size) to the length of string s1.
- Initialize a variable (matched) to keep track of the count of characters that are fully matched in the current window.

2) Character Frequency Dictionary Initialization:
- Iterate through each character in string s1.
- Populate the char_freq dictionary with the initial frequency of characters in s1.

3) Sliding Window Iteration:
- Iterate through each character in string s2 using a loop.
- For each character in s2:
    - Update the frequency of the current character in the sliding window (char_freq).
    - Check if the frequency of the character going out of the window has reached zero. If so, decrement the matched count.
    - If the window size is reached, update the frequency for the character going out of the window.

4) Check for Permutation:
- Check if the matched count is equal to the length of string s1.
If true, return True as a permutation of s1 is present in the current window.

5) Return Result


### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume `N` is the length of string `s2` and `M` is the length of string `s1`. 

- Time Complexity: O(N)
- Space Complexity: O(M)