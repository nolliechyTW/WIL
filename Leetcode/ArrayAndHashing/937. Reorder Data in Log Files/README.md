## 937. Reorder Data in Log Files
🔗  Link: [Reorder Data in Log Files](https://leetcode.com/problems/reorder-data-in-log-files/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, Sorting, String<br>

=======================================================================================<br>
You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.<br>

There are two types of logs:
- Letter-logs: All words (except the identifier) consist of lowercase English letters.
- Digit-logs: All words (except the identifier) consist of digits.


Reorder these logs so that:
- The letter-logs come before all digit-logs.
- The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
- The digit-logs maintain their relative ordering.
Return the *final* order of the logs.<br>

Example 1:<br>
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]<br>
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Explanation:<br>
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".<br>
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".<br>

Example 2:<br>
Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]<br>
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]<br>

Constraints:<br>
- 1 <= logs.length <= 100
- 3 <= logs[i].length <= 100
- All the tokens of logs[i] are separated by a single space.
- logs[i] is guaranteed to have an identifier and at least one word after the identifier.

=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Are there any edge cases in log formats that we should be aware of, such as logs that start with special characters or spaces?
    - No
2. Any requirement on time/space complexity?
    - O(n) time complexity and O(1) space complexity
3. Should the sorting of letter-logs be case-sensitive or case-insensitive?
4. Should digit-logs be treated as a single block, or is there any scenario where they could be intermixed with letter-logs based on certain conditions?

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. String Manipulation
The problem requires parsing each log entry to determine whether it's a letter-log or a digit-log. This involves understanding and manipulating strings, including splitting logs into their constituent parts (identifier and content) and analyzing the content to classify the log.

2. Sorting Algorithms with Custom Sorting Logic
The problem goes beyond standard sorting by requiring a custom comparison function. This custom logic must handle both the comparison of the contents of the letter-logs and the fallback to comparing identifiers when contents are equal.

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: 

1. Separate Logs: Iterate through each log entry and classify it as either a digit-log or a letter-log based on the content following the identifier. This classification is done by checking if the first character after the identifier is a digit.

2. Sort Letter-Logs: Sort the letter-logs by their contents, and in cases where contents are identical, use their identifiers as a secondary sorting criterion. This is achieved by using a custom sort key that first considers the log's content (excluding the identifier) and then the identifier itself.

3. Concatenate Logs: Combine the sorted letter-logs with the unsorted digit-logs, maintaining the original order of the digit-logs. Letter-logs, being sorted, are placed before the digit-logs in the final output.

4. Return Result

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N is the total number of logs and M is the average length of a log
- Time Complexity: O(NlogN×M), since these contents need to be split and compared, the actual comparison operation could have a complexity of O(M) for each comparison.
- Space Complexity: O(N),  where N is the total number of logs.