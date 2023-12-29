## 12. Integer to Roman
🔗  Link: [Integer to Roman](https://leetcode.com/problems/integer-to-roman/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: String, Math, Hashtable<br>

=======================================================================================<br>

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.<br>

| Symbol | Value |
|--------|-------|
|   I    |   1   |
|   V    |   5   |
|   X    |   10  |
|   L    |   50  |
|   C    |  100  |
|   D    |  500  |
|   M    | 1000  |

For example, `2` is written as `II` in Roman numeral, just two one's added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9. 
- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90. 
- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.


Example 1:<br>
Input: num = 3<br>
Output: "III"<br>
Explanation: 3 is represented as 3 ones.<br>

Example 2:<br>
Input: num = 58<br>
Output: "LVIII"<br>
Explanation: L = 50, V = 5, III = 3.<br>

Example 3:<br>
Input: num = 1994<br>
Output: "MCMXCIV"<br>
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.<br>

Constraints:<br>
- 1 <= num <= 3999<br>

=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. What is the range of integers that need to be converted? 
- 1 <= num <= 3999
2. Should the program handle cases where the input is not a valid integer, or integers that are outside the typical range for Roman numerals?
- Ignore this situation 
3. Any requirement on time/space complexity?
- As there is a finite set of roman numerals, there is a hard upper limit on how many times the loop can iterate.


### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


- Hashtable <br>
Roman numeral conversion involves mapping unique integer values to specific string representations. Hashtables are ideal for this type of one-to-one mapping.
Also, the order of elements is preserved in this data structure, which is really crucial for our Roman numeral conversion as we need to process the integers in descending order, from the largest to the smallest.

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Converts integers to Roman numerals using a subtractive technique, where it repeatedly subtracts the value of the largest possible Roman numeral from the number until it reaches zero, building the Roman numeral representation as it goes.<br>
1) Define a Mapping: It starts by defining a dictionary `roman_map` that serves as a mapping between the integer values and their corresponding Roman numeral symbols. This dictionary includes both the standard Roman numeral symbols and the subtractive combinations used for specific cases (like `IV` for 4, `IX` for 9, etc.).

2) Iterate Over Mapping: The method then iterates over the items in `roman_map`, which are key-value pairs where the key is the integer value and the value is the corresponding Roman numeral symbol.

3) Construct Roman Numeral: For each key-value pair, the method enters a `while` loop that continues as long as the input number `num` is greater than or equal to the current key (integer value) from the mapping. Inside the loop, the method subtracts the key from `num` and appends the corresponding Roman numeral symbol to the list `roman_numeral`.

4) Repeat Until Fully Converted: This process repeats, moving through the dictionary from the largest to the smallest values, effectively breaking down the input number into its Roman numeral components.

5) Combine Symbols: Finally, the list `roman_numeral` is concatenated into a single string using join, which represents the Roman numeral equivalent of the original integer.

6) Return the Result


### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

As there is a finite set of roman numerals, there is a hard upper limit on how many times the loop can iterate.

- Time Complexity: O(1)
- Space Complexity: O(1)
