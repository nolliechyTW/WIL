## 344. Reverse String
🔗  Link: [Reverse String](https://leetcode.com/problems/reverse-string/description/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: Two Pointers, String<br>

=======================================================================================<br>
Write a function that reverses a string. The input string is given as an array of characters `s`.<br>

You must do this by modifying the input array in-place with O(1) extra memory.<br>

Example 1:
Input: s = ["h","e","l","l","o"]<br>
Output: ["o","l","l","e","h"]<br>


Example 2:<br>
Input: s = ["H","a","n","n","a","h"]<br>
Output: ["h","a","n","n","a","H"]<br>



Constraints:<br>
- 1 <= s.length <= 10^5
- `s[i]` is a printable ascii character.=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. What kind of characters can the input string contain? Are they limited to ASCII characters, or does it include Unicode characters as well (like emojis, accented characters, etc.)?
    - `s[i]` is a printable ascii character.
2. Any requirement on time/space complexity? 
3. Should the function return anything, or is the sole requirement to modify the input array?
    - No need to return anything
4. How should the function handle an empty array?
    - It is guranteed that there will be at least one element in the array

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1.  Pointers <br>
The operation (reversing) is symmetric, meaning we need to swap elements from both ends towards the center. This naturally lends itself to a two-pointers approach where one pointer starts at the beginning and another at the end, and they move towards each other. Also the requirement for in-place modification means we cannot use extra space proportional to the input size. Two pointers work directly on the original array, swapping elements as they traverse, thereby not requiring additional space beyond the constant space for the pointers themselves.

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: reverse a string in-place using the two-pointers technique

1. Initilize Pointers:
- `left` and `right` pointers are initialized at the start and the end of the list
    - `left` is set to `0` (the first index)
    - `right` is set to `len(s)-1` (the last index)
2. While Loop
- as long as `left` is less than `right`, the elements at the left and right indices are swapped
- after each swap, update pointers

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the length of the string `s`


- Time Complexity: O(N), because the function uses a single loop that iterates approximately n/2 times 
- Space Complexity: O(1)
