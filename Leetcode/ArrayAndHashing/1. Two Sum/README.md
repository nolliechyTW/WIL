## 1. Two Sum
🔗  Link: [Two Sum](https://leetcode.com/problems/two-sum/description/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: Array, Hashmap<br>

=======================================================================================<br>
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:<br>
Input: nums = [2,7,11,15], target = 9<br>
Output: [0,1]<br>
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].<br>

Example 2:<br>
Input: nums = [3,2,4], target = 6<br>
Output: [1,2]<br>

Example 3:<br>
Input: nums = [3,3], target = 6<br>
Output: [0,1]<br>

Constraints:<br>
2 <= nums.length <= 10^4<br>
-10^9 <= nums[i] <= 10^9<br>
-10^9 <= target <= 10^9<br>
Only one valid answer exists.<br>
=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the nums array be empty?
2. Any requirement on time/space complexity?
3. Is the array sorted?
4. Will the numbers in the array duplicate?

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Sort<br>
Sort will not help becuase we need to return the index of the elements<br>
2. Dict/ hashmap <br>
Using a hashmap to store the elements of the array enables us to efficiently maintain the association between indices and values, where each value is paired with its corresponding index (key: value)

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Create a hashmap to store index and number so that we can refer to the hashmap for the index once we find the counterpart.

1) Create a hashmap
2) Iterate through the array
    - If we see the counterpart in our hashmap then return the index of the counterpart and current index.
    - Else Store the counterpart of the number we have seen and current index.
    - It is said that there is exactly one solution.
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the number of items in the array.


- Time Complexity: O(N)
- Space Complexity: O(N)
