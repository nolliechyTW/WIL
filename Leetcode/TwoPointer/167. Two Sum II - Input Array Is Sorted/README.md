## 167. Two Sum II - Input Array Is Sorted
🔗  Link: [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Two Pointers, Array, Binary Search<br>

=======================================================================================<br>
Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where 1 <= `index1` < `index2` < `numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, added by one as an integer array `[index1, index2]` of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Example 1:<br>
Input: numbers = [2,7,11,15], target = 9<br>
Output: [1,2]<br>
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2]<br>

Example 2:<br>
Input: numbers = [2,3,4], target = 6<br>
Output: [1,3]<br>
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3]<br>

Example 3:<br>
Input: numbers = [-1,0], target = -1<br>
Output: [1,2]<br>
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].<br>


Constraints:<br>
2 <= numbers.length <= 3 * 10^4<br>
-1000 <= numbers[i] <= 1000<br>
numbers is sorted in non-decreasing order.<br>
-1000 <= target <= 1000<br>
The tests are generated such that there is exactly one solution.<br>
=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input array be empty? 
    - No, there is exactly one solution
2. Any requirement on time/space complexity? 
    - Your solution must use only constant extra space


### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1.  Left and Right Pointers <br>
We can employ two pointers: one starting from the left and the other starting from the right. If the sum of the numbers pointed to by these two pointers is excessive, we make adjustments to the right pointer. Conversely, if the sum is insufficient, we modify the position of the left pointer, continuing this process until we successfully reach the target value.

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Start traversing inwards, from both ends of the input string, and we can expect to see the same characters, in the same order

1) Initialize two pointer variables, left and right, and point them to the two ends of the input array
2) Check if the sum of the numbers pointed to by these two pointers is equal to the target
    - If it is equal, add 1 to the index since the question is 1-indexed, add them to the ans array, and return ans
    - If it is too large, decrement the right pointer by 1
    - Otherwise, increment the left pointer by 1 since it is too small

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the number of numbers in the array.


- Time Complexity: O(N)
- Space Complexity: O(1)
