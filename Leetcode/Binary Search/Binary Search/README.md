## 704. Binary Search
🔗  Link: [Binary Search](https://leetcode.com/problems/binary-search/description/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: Array, Binary Search<br>

=======================================================================================<br>
Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

Example 1:<br>
Input: nums = [-1,0,3,5,9,12], target = 9<br>
Output: 4<br>
Explanation: 9 exists in nums and its index is 4<br>

Example 2:<br>
Input: nums = [-1,0,3,5,9,12], target = 2<br>
Output: -1<br>
Explanation: 2 does not exist in nums so return -1<br>

Constraints:<br>
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All the integers in `nums` are unique
- `nums` is sorted in ascending order

=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input string be empty? 
2. Any requirement on time/space complexity? 
    - You must write an algorithm with O(log n) runtime complexity.
3. Test case: <br>
    Input: nums = [5], target = 5<br>
    Output: 0<br>


### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. Binary Search <br>
Binary search is a method for locating an element in a sorted list efficiently. Searching for an element can be done naively in O(N) time, but binary search speeds it up to O(log N).


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

- General Idea: <br>
    ```
    def binary_search(nums, key):
        if nums is empty:
            return None
        if middle element is equal to key:
            return middle index
        if middle element is greater than key:
            binary search left half of nums
        if middle element is less than 
            binary search right half of nums
    ```

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the number of elements in the array.


- Time Complexity: O(logN), because each iteration decreases the size of the list by a factor of 2
- Space Complexity: O(1)
