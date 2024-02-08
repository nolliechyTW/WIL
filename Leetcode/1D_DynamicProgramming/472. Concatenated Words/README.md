## 472. Concatenated Words
🔗  Link: [Concatenated Words](https://leetcode.com/problems/concatenated-words/description/)<br>
💡 Difficulty: Hard<br>
🛠️ Topics: DP, DFS, String<br>

=======================================================================================<br>
Given an array of strings `words` (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words (not necessarily distinct) in the given array.<br>


Example 1:<br>
Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog",<br>"hippopotamuses","rat","ratcatdogcat"]<br>
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]<br>
Explanation: <br>
"catsdogcats" can be concatenated by "cats", "dog" and "cats"; <br>
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; <br>
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat"<br>

Example 2:<br>
Input: words = ["cat","dog","catdog"]<br>
Output: ["catdog"]<br>

Constraints:<br>
- 1 <= words.length <= 10^4
- 1 <= words[i].length <= 30
- words[i] consists of only lowercase English letters.
- All the strings of words are unique.
- 1 <= sum(words[i].length) <= 10^5

=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. When determining if a word is concatenated from other words in the list, can the same word from the list be used more than once in the concatenation? For example, if "star" is in the list, can "starstar" be considered a concatenated word?
    - Yes, the same word from the list can be used more than once in the concatenation, as long as the final word is comprised of at least two words from the list
2. Is there a minimum or maximum length for the words in the input array? Understanding the range of word lengths could impact the choice of algorithm or optimizations
3. Should the solution be case-sensitive? For instance, if "Hello" and "World" are in the list, should "helloworld" be considered a concatenated word, or is case matching required?
    - The solution should typically be case-sensitive


### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1)  Dynamic Programming and Memoization Approach
    - A word is concatenated if at least one valid split exists where the prefix is a word in the list (or is itself concatenated) and the suffix is either a word in the list or can be further split into concatenated words. This characteristic allows for a DP approach, where the solution to the larger problem depends on the solutions to its subproblems
    - When checking if a word is concatenated, the same suffixes or prefixes may be checked multiple times for different words. Memoization stores these results, so they don't have to be recomputed


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Determine which words in the input list can be formed by concatenating two or more other words from the same list. This is not about simple string concatenation; it involves partitioning the word into segments where each segment is a valid word in the list, and the whole constitutes the original word

1. Initialization:
- Convert the list of `words` into a set (`setofWords`) for O(1) lookup times
- Prepare an empty list (`ans`) to store the final list of concatenated words
- Create a dictionary (`memo`) to **cache the results of sub-problems**

2. Define a Recursive Function (dfs):
- This function attempts to determine if a word can be considered a concatenated word by recursively checking if it can be split into a prefix and suffix where the prefix is a word in the list, and the suffix either is a word in the list or can be further split into concatenated words
- For each word, it iterates through all possible splits (from the 1st character to the last), checks if the prefix is in the set of words, and then checks if the suffix is either in the set or can be split further into valid words (recursive call to dfs)
- The result of each check (True if the word is a concatenated word, False otherwise) is stored in the `memo` dictionary to avoid recalculating for the same word segment

3) Iterate Through Each Word in the List:
- For each word, it checks if the word is non-empty and then calls the dfs function on it
- If dfs returns True (indicating the word can be constructed from other words in the list), the word is added to the ans list

4) Return the Result:
After iterating through all words, the list ans containing all concatenated words is returned.


### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume there are `N` word in the strings.

- Time Complexity: 
- Space Complexity: 