## 3. Longest Substring Without Repeating Characters
🔗  Link: [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: String, Hash, Sliding Window<br>

=======================================================================================<br>
Given a string `s`, find the length of the longest substring without repeating characters.<br>

Example 1:<br>
Input: s = "abcabcbb"<br>
Output: 3<br>
Explanation: The answer is "abc", with the length of 3.<br>

Example 2:<br>
Input: s = "bbbbb"<br>
Output: 1<br>
Explanation: The answer is "b", with the length of 1.<br>

Example 3:<br>
Input: s = "pwwkew"<br>
Output: 3<br>
Explanation: The answer is "wke", with the length of 3.<br>
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.<br>


Constraints:<br>
- 0 <= s.length <= 5 * 10^4
- `s` consists of English letters, digits, symbols and spaces.

=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input string be empty? What should I return for an empty string?
    - Yes. Simply return `0`
2. Any requirement on time/space complexity?
    - You must write an algorithm that runs in O(n) time and O(1) space
3. Should the solution be case-sensitive? In other words, are 'A' and 'a' considered the same character or different?
    - The solution should be case-sensitive

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. Sliding Window <br>
The problem asks for a "longest substring," which is a continuous sequence of characters. The sliding window technique is perfect for such scenarios because it can dynamically resize and slide through the string to capture different substrings.

2. HashSet<br>
The set is a perfect tool for tracking unique characters. It provides O(1) time complexity for add, remove, and check operations, which are exactly what you need when you want to quickly check if a character has already been seen in the current substring.

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: As we iterate through the string, we adjust the window's size and position based on the uniqueness of characters (as tracked by the set). When a repeat character is found, we move the start of the window right past the first occurrence of that character, thus maintaining the "no repeating characters" condition. The maximum size of the window during this process is the length of the longest substring without repeating characters.


1) Initialize Variables
    - Create a set named `seen` to keep track of unique characters
    - Initialize an integer `left` to 0 to mark the start of the sliding window
    - Initialize an integer `ans` to 0 to store the length of the longest substring found
2) Iterate Through the String
    - Use a for-loop to iterate through the string `s`, with `right` as the loop variable starting from `0` up to the length of `s - 1`
3) Check and Remove Repeating Characters
    - Inside the loop, check if the character at index `right` in `s` is already in the set `seen`
    - If it is, enter a while loop:
        - Remove the character at index `left` from the set `seen`
        - Increment `left` by `1` (move the start of the sliding window to the right)
4) Add New Character and Update Maximum Length
    - Add the character at index `right` to the set `seen`
    - Update `ans` with the maximum value between its current value and the current window size (calculated by `right - left + 1`)
5) Return the Result


### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the number of chars in the string.

- Time Complexity: O(N)
- Space Complexity: O(1)
