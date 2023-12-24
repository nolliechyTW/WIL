## 1151. Minimum Swaps to Group All 1's Together
🔗  Link: [Minimum Swaps to Group All 1's Together](https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, Sliding Window<br>

=======================================================================================<br>
Given a binary array `data`, return the minimum number of swaps required to group all `1`’s present in the array together in *any place* in the array.<br>


Example 1:<br>
Input: data = [1,0,1,0,1]<br>
Output: 1<br>
Explanation: There are 3 ways to group all 1's together:<br>
[1,1,1,0,0] using 1 swap.<br>
[0,1,1,1,0] using 2 swaps.<br>
[0,0,1,1,1] using 1 swap.<br>
The minimum is 1.<br>

Example 2:<br>
Input: data = [0,0,0,1,0]<br>
Output: 0<br>
Explanation: Since there is only one 1 in the array, no swaps are needed.<br>

Example 3:<br>
Input: data = [1,0,1,0,1,0,0,1,1,0,1]<br>
Output: 3<br>
Explanation: One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].<br>

Constraints:<br>
- 1 <= data.length <= 10^5
- data[i] is either 0 or 1
=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Could you clarify what constitutes a swap in this context? For example, is swapping adjacent elements the only allowed operation, or can elements be swapped from any position in the array?
    - elements can be swapped from any position in the array
2. Any requirement on time/space complexity?
    - O(n) time complexity and O(1) space complexity

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. Sliding Window<br>
The sliding window technique enables you to solve the problem in linear time (O(n)). As the window slides through the array, you only need to update the count of 1s or 0s at the entering and exiting edges of the window, rather than recalculating the entire count within the window

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: use a sliding window approach to find the maximum number of contiguous 1's and returns the difference between the total number of 1's and this maximum


### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N is the length of the array.

- Time Complexity: O(N)
- Space Complexity: O(1)