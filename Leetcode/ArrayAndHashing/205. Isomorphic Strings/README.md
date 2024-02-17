## 205. Isomorphic Strings
🔗  Link: [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/description/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: Array, HashTable<br>

=======================================================================================<br>
Given two strings `s` and `t`, determine if they are isomorphic.<br>

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.<br>

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.<br>


Example 1:<br>
Input: s = "egg", t = "add"<br>
Output: true<br>


Example 2:<br>
Input: s = "foo", t = "bar"<br>
Output: false<br>

Example 3:<br>
Input: s = "paper", t = "title"<br>
Output: true<br>


Constraints:<br>
- 1 <= s.length <= 5 * 10^4<br>
- t.length == s.length<br>
- `s` and `t` consist of any valid ascii character.<br>


=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input array be empty?
    - No, the minimum interval length is 1
2. Any requirement on time/space complexity?
    - O() time and O(1) space not including the resulting output array
3. Are two strings guaranteed to have a same size? 
    - Yes
4. Are the strings s and t composed of ASCII characters only, or do we need to account for Unicode characters as well?
    - ascci characters only 
5. Should the isomorphism check be case-sensitive?
    - Yes, upper and lower case characters should be trated as distinct

 
### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. Hashtable <br>
Using a hashmap in this problem efficiently helps us map characters from one string to characters in another string. With a hashmap, both the insertion of a new mapping and the lookup to check existing mappings are performed in O(1) average time complexity, making the overall algorithm more efficient.


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: maintain two mappings: one from characters in s to characters in t, and another from characters in t to characters in s. This ensures that each character in one string maps to a unique character in the other string, which is a requirement for two strings to be isomorphic. <br>


1) Initialize Two Hashmaps: Begin by creating two hashmaps. The first hashmap tracks mappings from characters in string `s` to corresponding characters in string `t`, and the second hashmap does the reverse, mapping characters from `t` to `s`. This dual mapping ensures that the relationship between characters is one-to-one and not merely one-way.

2) Iterate Over the Strings Concurrently: **Use the `zip() `function to iterate over both strings simultaneously**. This allows you to examine corresponding characters from *`s` and `t` at each step of the iteration*, ensuring that your comparisons and mappings are based on the correct character positions.
    - if a character pair (character from s and its counterpart from t) does not exist in the hashmaps, add this new mapping to both hashmaps. This step establishes a mutual mapping between characters that have not been encountered before.
    - if the characters being examined are already present in the hashmaps, confirm that the existing mappings are consistent with the current character pair. 
        - If the current characters do not conform to the previously established mappings, the strings are not isomorphic.

3) Return True if Isomorphic: If the algorithm completes without finding any inconsistencies in the mappings, conclude that the strings are isomorphic. <br>


### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume 'N' is the length of both string `s` and `t`.
- Time Complexity: O(N)
- Space Complexity: O(N)
