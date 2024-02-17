## 209. Minimum Size Subarray Sum
🔗  Link: [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, Sliding Window<br>

=======================================================================================<br>
Given an array of positive integers `nums` and a positive integer `target`, return the **minimal length** of a subarray whose sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.<br>

**Follow up:** If you have figured out the O(n) solution, try coding another solution of which the time complexity is `O(n log(n))`.<br>

Example 1:<br>
Input: target = 7, nums = [2,3,1,2,4,3]<br>
Output: 2<br>
Explanation: The subarray [4,3] has the minimal length under the problem constraint.<br>


Example 2:<br>
Input: target = 4, nums = [1,4,4]<br>
Output: 1<br>


Constraints:<br>
- 1 <= target <= 10^9
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4
=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input array be empty?
    - No, there is at least 1 element in the array
2. Any requirement on time/space complexity?
    - If you have figured out the `O(n) `solution, try coding another solution of which the time complexity is `O(n log(n))`
3. Is the array sorted by it's elements order?
    - No
4. Will there be negative numbers in the array?
    - both target and numbers in the array are guaranteed to be positive numbers

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. Sliding Window<br>
- The two-pointer or sliding window technique is particularly suited for problems involving contiguous subarrays in an array, especially when the goal is to optimize for certain conditions like minimal length, maximal sum, etc.
- This technique allows the size of the window (subarray) to dynamically adjust based on the running sum compared to the target. By moving the right pointer, you increase the window size and the sum; by moving the left pointer, you decrease them. 

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: utilize a sliding window to explore different segments of the array without the need to check every possible subarray explicitly. This sliding window is dynamically adjusted based on the cumulative sum of its elements relative to the target sum. 

1) Initialization:
- Start with an infinite value for the answer (`ans`) to ensure any valid window found will be smaller than this initial value. 
- Initialize a variable to keep track of the current sum (`currSum`) of elements within the window
- Initialize a variable, a left pointer (`left`), to mark the start of the window.

2) Iterate Through the Array: 
- Use a for-loop to iterate over the array with a right pointer (`right`). 
- For each element encountered, add it to `currSum`, effectively extending the window to the right.

3) Adjust the Window: 
- Whenever `currSum` equals or exceeds the `target`, attempt to **shrink the window from the left** to find the smallest possible window that still meets the condition. This is done by:
    - Updating `ans` with the current window size if it is smaller than the previously recorded answer.
    - Subtracting the value at the left pointer from currSum and then incrementing the left pointer, effectively shrinking the window from the left side.
4) Result: 
- After examining all elements, check if ans was updated from its initial infinite value. 
    - If so, return `ans` as the minimal length of a subarray meeting the condition. 
    - If `ans` remains infinite, it means no such subarray exists, and the function returns `0`.

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

- Time Complexity: O(N)
- Space Complexity: O(1)
