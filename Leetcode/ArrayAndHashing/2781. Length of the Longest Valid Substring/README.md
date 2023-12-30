## 2781. Length of the Longest Valid Substring
🔗  Link: [Length of the Longest Valid Substring](https://leetcode.com/problems/length-of-the-longest-valid-substring/description/)<br>
💡 Difficulty: Hard<br>
🛠️ Topics: String, Array, Hashtable<br>

=======================================================================================<br>

You are given a string word and an array of strings `forbidden`.

A string is called **valid** if none of its substrings are present in `forbidden`.

Return the length of the **longest valid substring** of the string `word`.

A substring is a contiguous sequence of characters in a string, possibly empty.


Example 1:<br>
Input: word = "cbaaaabc", forbidden = ["aaa","cb"]<br>
Output: 4<br>
Explanation: There are 11 valid substrings in word: "c", "b", "a", "ba", "aa", "bc", "baa", "aab", "ab", "abc" and "aabc". The length of the longest valid substring is 4. <br>
It can be shown that all other substrings contain either "aaa" or "cb" as a substring. <br>


Example 2:<br>
Input: word = "leetcode", forbidden = ["de","le","e"]<br>
Output: 4<br>
Explanation: There are 11 valid substrings in word: "l", "t", "c", "o", "d", "tc", "co", "od", "tco", "cod", and "tcod". The length of the longest valid substring is 4.<br>
It can be shown that all other substrings contain either "de", "le", or "e" as a substring. <br>



Constraints:<br>
- 1 <= word.length <= 10^5
- `word` consists only of lowercase English letters.
- 1 <= forbidden.length <= 10^5
- 1 <= forbidden[i].length <= 10
- `forbidden[i]` consists only of lowercase English letters.<br>

=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Should the comparison between substrings of `word` and elements in `forbidden` be case-sensitive? 
- both `word` and `forbidden` only contan lowercase English letters
2. What is the expected size of word and forbidden? Knowing this can help in optimizing the algorithm for larger inputs.
- `forbidden[i]` will only consist 10 characters at most
3. Any requirement on time/space complexity?
- O(n) in time


### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


- Sliding Window <br>
The problem requires identifying valid substrings within a given string. A substring is inherently a contiguous block of characters within a larger string. The sliding window technique is well-suited for dealing with contiguous sequences or blocks of data within a larger dataset. Also, the objective is to find the longest valid substring. The sliding window allows for an iterative examination of each possible substring in word, while efficiently keeping track of the maximum length of valid substrings found so far.<br>

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use a sliding window approach along with efficient substring checking. For each position of the right pointer, the code checks whether any substring ending at the right pointer and within a length of up to 10 characters (or up to the left pointer, whichever is shorter) is forbidden.<br>

1) Initialize:
- Convert the `forbidden` list into a set (`setF`) for efficient substring lookups.
- Set `res` (result) to 0, representing the length of the longest valid substring found.
- Initialize two pointers, `left` and `right`, both set to 0. These pointers define the current window of the string being analyzed.

2) Iterate Through the String:
Use the `right` pointer to iterate through each character in the string word.

3) Check for Forbidden Substrings:
- For each position of the right pointer, **iterate backwards from right to the maximum of left - 1 and right - 10** (to check a maximum of 10 characters backwards).
- During this backward iteration, check if any substring from index `i` to `right` is in the forbidden set (`setF`).

4) Update the Window:
- If a forbidden substring is found, move the `left` pointer to the position just after the end of this forbidden substring (i.e., `left = i + 1`).
- Break the inner loop to stop checking further substrings for the current position of `right`.

5) Update the Result:
After each iteration of the `right` pointer, update `res` to the maximum of its current value and the length of the current window (`right - left + 1`).

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

Assume N is the length of the input `word` and M is the number of `forbidden` substrings.

- Time Complexity: O(N)
- Space Complexity: O(M)
