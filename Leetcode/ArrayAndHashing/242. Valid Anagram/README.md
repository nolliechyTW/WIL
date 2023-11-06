## 242. Valid Anagram
🔗  Link: [Valid Anagram](https://leetcode.com/problems/valid-anagram/description/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: String, Sort, HashTable<br>

=======================================================================================<br>
Given two strings `s` and `t`, return true if `t` is an anagram of `s`, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:<br>
Input: s = "anagram", t = "nagaram"<br>
Output: true<br>

Example 2:<br>
Input: s = "rat", t = "car"<br>
Output: false<br>

Constraints:<br>
1 <= s.length, t.length <= 5 * 10^4 <br>
`s` and `t` consist of lowercase English letters.
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
