## 49. Group Anagrams
🔗  Link: [Group Anagrams](https://leetcode.com/problems/group-anagrams/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, Sort, Hash<br>

=======================================================================================<br>
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.<br>
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:<br>
Input: strs = ["eat","tea","tan","ate","nat","bat"]<br>
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]<br>


Example 2:<br>
Input: strs = [""]<br>
Output: [[""]]<br>

Example 3:<br>
Input: strs = ["a"]<br>
Output: [["a"]]<br>

Constraints:<br>
1 <= strs.length <= 104<br>
0 <= strs[i].length <= 100<br>
strs[i] consists of lowercase English letters.<br>
=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input array be empty?
2. Any requirement on time/space complexity?
3. Is the array sorted? If not, is sorting a costly operation?
 
### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. Sort <br>
This can work if the given string in the array can be sorted. We can sort the character in the string and compare each of them since **two strings are anagrams if and only if their sorted strings are equal**.

2. Storing the elements of the array in a HashMap<br>
As we sort the string, we can maintain a map `"sorted string": [list of strings having the same key]`.



### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Create a map to associate sorted strings (keys) with the original input strings (values). After populating the map, return the values as a list of lists.

1. Initialize a map.
2. Iterate through the list of strings:
- If a string's sorted version is already a key in the map, append the string to the corresponding list.
- Else, create a new key-value pair.
3. Return the values as a list with `.value()`, converting them with `list()`.


### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N is the length of strs and K is the maximum length of a string in strs.

- Time Complexity: O(NKlogK)
- Space Complexity: O(NK)
