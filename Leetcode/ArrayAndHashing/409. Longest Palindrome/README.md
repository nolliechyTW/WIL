## 409. Longest Palindrome
🔗  Link: [Longest Palindrome](https://leetcode.com/problems/longest-palindrome/description/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: HashTable, String<br>

=======================================================================================<br>
Given a string `s` which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.<br>

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:<br>
Input: s = "abccccdd"<br>
Output: 7<br>
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.<br>

Example 2:<br>
Input: s = "a"<br>
Output: 1<br>
Explanation: The longest palindrome that can be built is "a", whose length is 1.<br>

Constraints:<br>
- 1 <= s.length <= 2000<br>
- `s` consists of lowercase and/or uppercase English letters only.

=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input be empty?
- No, assume there is at least one character in the string
2. Any requirement on time/space complexity?
- O(N) in time, O(1) in space
3. Are there any restrictions on the use of additional data structures?
-  No


### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


- Hashtable <br>
    1) The problem requires keeping track of whether each character has been seen an odd or even number of times. A hashtable is well-suited for **tracking occurrences** of elements because it can directly associate each unique element (in this case, characters) with data (like its count or presence)
    2) Since the problem involves letters that are case-sensitive, the maximum number of unique keys (characters) is limited (26 lowercase + 26 uppercase letters in the English alphabet). This constraint makes a hashtable an even more appealing choice, as the space complexity remains manageable

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: A key point to note is that in a palindrome, every letter appears an even number of times, except for possibly one letter, which can appear an odd number of times (in the center of the palindrome)

1) Initialize variables
    - Initialize `pairedCharsCount` to 0
    - Initialize `unpaired_chars` as an empty set

2) Iterate each character char in string `s`
    - Check if 'char' is present in the unpaired_chars set:
        - If it is, it means we've found a pair for 'char'
        - Increment the pairedCharsCount by 1, as we've found another pair
        - Remove 'char' from unpaired_chars set, as it's now paired

    - If 'char' is not in the unpaired_chars set:
        - Add 'char' to the unpaired_chars set, as it's an unpaired character for now

3) After the loop ends, check if there are any unpaired characters left
    - If unpaired_chars is not empty:
        - We can use one unpaired character as the middle character in the palindrome
        - Therefore, return the total count of characters that can be used in the palindrome, which is twice the pairedCharsCount (as each pair contributes two characters) plus 1 for the middle character

    - If unpaired_chars is empty:
        - All characters are paired, and we can't use any character as a middle character
        - Thus, return twice the pairedCharsCount, as each pair contributes two characters to the palindrome


### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the number of char in the string `s`.


- Time Complexity: O(N)
- Space Complexity: O(1)
