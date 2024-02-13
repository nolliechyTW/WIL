## 139. Word Break
🔗  Link: [Word Break](https://leetcode.com/problems/word-break/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, DP<br>

=======================================================================================<br>
Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

<br>

Example 1:<br>
Input: s = "leetcode", wordDict = ["leet","code"]<br>
Output: true<br>
Explanation: Return true because "leetcode" can be segmented as "leet code".<br>

Example 2:<br>
Input: s = "applepenapple", wordDict = ["apple","pen"]<br>
Output: true<br>
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".<br>
Note that you are allowed to reuse a dictionary word.<br>

Example 3:<br>
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]<br>
Output: false<br>

Constraints:<br>
- 1 <= s.length <= 300
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 20
- s and wordDict[i] consist of only lowercase English letters.
- All the strings of wordDict are unique.<br>


=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Any requirement on time/space complexity?
- O(N^3) in time and O(N) in space
2. Can there be multiple valid solutions?
- Yes, there may be multiple valid solutions. If so, the end result will still be the same, so the specific solution path does not matter much.

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1)  Dymanic Programming <br>
    - **DP builds up the solution by considering smaller subproblems**. It explores all combinations, ensuring that the global optimal solution is found
    - The intuition behind this approach is that the given problem (s) can be divided into subproblems s1 and s2. If these subproblems individually satisfy the required conditions, the complete problem, s also satisfies the same. e.g. "catsanddog" can be split into two substrings "catsand", "dog". The subproblem "catsand" can be further divided into "cats","and", which individually are a part of the dictionary making "catsand" satisfy the condition


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use a DP Array to check if any substring from i -> j is in the word bank. Build up this solution to the last index of the input string (Bottom-Up Approach). In this case, the subproblem is determining if a prefix of the string can be segmented into words from the dictionary

1) Convert Dictionary to Set
- Convert the list of dictionary words (`wordDict`) into a set (`wordSet`) for efficient look-up operations

2) Initialize Dynamic Programming Array
- Create a boolean array `dp` of length `len(s) + 1`, where each element `dp[i]` indicates whether the `substring s[:i]` can be segmented into words from `wordSet`. Initialize `dp[0]` to `True` to represent that an empty string is considered segmentable.

3) Iterate Over the String
- For each position `i` in the string `s` (starting from 1 to len(s)), perform the following steps:
    - Check for Word Matches: Iterate through each word in `wordSet` and for each word, check if the word can fit ending at position i in the string s. This involves checking if `dp[i - wordLen]` is `True` (indicating that the substring `s[:i - wordLen]` can be segmented) and if the substring `s[i - wordLen:i]` matches the current word from `wordSet`.
    - Update DP Array: If both conditions are met, set `dp[i]` to `True`, indicating that `s[:i]` can be segmented into dictionary words. Once `dp[i]` is set to `True`, break the inner loop to avoid unnecessary checks for this position `i`.

4) Return Result: 
- After completing the iterations, return the value of `dp[-1]`. This value indicates whether the entire string s can be segmented into a sequence of dictionary words. If `dp[-1]` is `True`, it means s can be fully segmented using the words in the dictionary. If it's `False`, s cannot be segmented entirely using the dictionary words.


### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume `N` is the length of the input string

- Time Complexity: O(N^3)
- Space Complexity: O(N)
