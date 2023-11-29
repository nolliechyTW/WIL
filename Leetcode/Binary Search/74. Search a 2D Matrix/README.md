## 74. Search a 2D Matrix
🔗  Link: [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, Binary Search, Matrix<br>

=======================================================================================<br>
You are given an m x n integer `matrix` with the following two properties:

- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.
Given an integer `target`, return `true` if `target` is in matrix or `false` otherwise.


Example 1:<br>
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3<br>
Output: true<br>

Example 2:<br>
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13<br>
Output: false<br>

Constraints:<br>
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 100
- -10^4 <= matrix[i][j], target <= 10^4

=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input matrix be empty? 
    - We don’t need to consider empty inputs
2. Any requirement on time/space complexity? 
    - You must write a solution in O(log(m * n)) time complexity and O(1) space complexity
3. Can the row size be different from the column size?
    - Yes, the row size can be different from the column size


### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. Binary Search <br>
Binary search is a method for locating an element in a sorted list efficiently. Searching for an element can be done naively in O(N) time, but binary search speeds it up to O(log N).


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

- General Idea: consider 2d as 1d and we can simply apply binary search to search the target
1) Determine the number of `rows` and `columns` by obtaining the lengths, allowing us to calculate the total number of elements using rows multiplied by columns, and then subtracting one
2) Utilize binary search to find the target value within the matrix:
    - Define the `mid_value` as `matrix[mid//cols][mid%cols]`
    - If `mid_value` is greater than the `target`, adjust the right pointer
    - If `mid_value` is smaller than the `target`, adjust the left pointer
3) If a `mid_value` equal to the `target` is successfully found, return `True`; otherwise, return `False`


### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Given an m x n integer `matrix`.

- Time Complexity: O(log(m * n))
- Space Complexity: O(1)
