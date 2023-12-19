## 2405. Optimal Partition of String
🔗  Link: [Optimal Partition of String](https://leetcode.com/problems/optimal-partition-of-string/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Hashtable, String, Greedy<br>

=======================================================================================<br>
Given a string `s`, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.<br>

Return the minimum number of substrings in such a partition.<br>

Note that each character should belong to exactly one substring in a partition.<br>

Example 1:<br>
Input: s = "abacaba"<br>
Output: 4<br>
Explanation:<br>
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").<br>
It can be shown that 4 is the minimum number of substrings needed.<br>

Example 2:<br>
Input: s = "ssssss"<br>
Output: 6<br>
Explanation:<br>
The only valid partition is ("s","s","s","s","s","s").<br>

Constraints:<br>
- 1 <= s.length <= 10^5
- `s` consists of only English lowercase letters.
=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. How should the function handle an empty string? Should it return 0 or handle it in some other way?
    - Assume there is always at least one character in the string 
2. Any requirement on time/space complexity?
    - O(n) time complexity and O(1) space complexity

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. Hashset<br>
A HashSet inherently ensures that all elements are unique. This aligns perfectly with the requirement that each substring must contain unique characters. 


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Iterates through the characters of the string, using a set to track unique characters and incrementing a counter.Whenever a repeated character is encountered, we signal the start of a new substring.
1) Initilize variables `temp` to store unique character and `ans` to represent the minimum number of substrings needed
2) Iterate through the string
    - Check for repeated characters
        - If `char` is in `temp`, it means the current substring has ended, and a new one should begin
            - Increment `ans` by 1, indicating the start of a new substring
            - Reset `temp` to an empty set to start tracking characters for the new substring
    - Add the current character to the set
3) Return `ans`, which now holds the total number of substrings needed

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N is the length of the string s.

- Time Complexity: O(N)
- Space Complexity: O(1), at most size = 26
