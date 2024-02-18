## 290. Word Pattern
🔗  Link: [Word Pattern](https://leetcode.com/problems/word-pattern/description/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: Hashmap, String<br>

=======================================================================================<br>
Given a pattern and a string `s`, find if `s` follows the same pattern.

Here follow means a full match, such that there is a **bijection** between a letter in pattern and a non-empty word in `s`.

Example 1:<br>
Input: pattern = "abba", s = "dog cat cat dog"<br>
Output: true<br>

Example 2:<br>
Input: pattern = "abba", s = "dog cat cat fish"<br>
Output: false<br>

Example 3:<br>
Input: pattern = "aaaa", s = "dog cat cat dog"<br>
Output: false<br>


Constraints:<br>
- 1 <= pattern.length <= 300
- pattern contains only lower-case English letters.
- 1 <= s.length <= 3000
- s contains only lowercase English letters and spaces ' '.
- s does not contain any leading or trailing spaces.
- All the words in s are separated by a single space.

=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the    are aligned on the expected inputs and outputs.
1. Does every character map to a single word?
- Each character has to map to a single word. Every word has to map to a single character.
2. Should the time and space complexity analyses ignore the size of words?
- Since the size (number of entries) of the two hash maps should be the same, it should be O(1). Whenever the number of distinct words goes beyond the number of distinct letters in the pattern, a False value will be returned immediately.
3. Are there any restrictions on the use of additional data structures?
-  No, but you should use hashmap to solve this problem


### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


- Hashmap<br>
1) A hashmap naturally represents the bijection needed between the characters in the pattern and the words in s. It allows you to easily establish and retrieve the one-to-one mapping required for the problem, ensuring that each character maps to exactly one word, and vice versa.

2) Hashmaps provide average constant time complexity, O(1), for both insertion and lookup operations.



### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: maps each character in pattern to a word in s and ensures that this mapping is both one-to-one and onto, fulfilling the bijection requirement.


1. For each (character and word) in the lists respectively, check if the mapping of char to word is in the dictionary (and similar for word to char). 
2. If the dictionary doesn’t yet have the mapping, add to it.
3. If at any instance, the mapping doesn’t match, return false. 
4. If after checking every pair, we still match, that means the pattern matches.

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the number of char/ words in the string `pattern` / `s`.


- Time Complexity: O(N)
- Space Complexity: O(N)
  