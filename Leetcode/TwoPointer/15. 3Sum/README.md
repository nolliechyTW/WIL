## 15. 3Sum
🔗  Link: [3Sum](https://leetcode.com/problems/3sum/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Two Pointers, Array<br>

=======================================================================================<br>
Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that i != j, i != k, and j != k, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets

Example 1:<br>
Input: nums = [-1,0,1,2,-1,-4]<br>
Output: [[-1,-1,2],[-1,0,1]]<br>
Explanation: <br>
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.<br>
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.<br>
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.<br>
The distinct triplets are [-1,0,1] and [-1,-1,2].<br>
Notice that the order of the output and the order of the triplets does not matter.<br>

Example 2:<br>
Input: nums = [0,0,0]<br>
Output: [[0,0,0]]<br>
Explanation: The only possible triplet sums up to 0.<br>


Constraints:<br>
3 <= nums.length <= 3000<br>
-10^5 <= nums[i] <= 10^5<br>
=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input array be empty? 
    - No, there is exactly one solution
2. Any requirement on time/space complexity? 
3. Is the input array sorted?
    - No
4. Can I modify it e.g. sort the array?
    - Yes
5. What should I return if no triplet meet the requirement?
    - Just []
        Example 3:<br>
        Input: nums = [0,1,1]<br>
        Output: []<br>
        Explanation: The only possible triplet does not sum up to 0.<br>

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1.  Sort<br>
When we sort the array first, we can skip repeated values.

2. Pointers <br>
Since duplicate values will be next to each other, it's easy to skip them using pointers. 

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Start traversing inwards, from both ends of the input string, and we can expect to see the same characters, in the same order

1) Sort the input array.
2) Initialize two pointers, `left` and `right`, where `left` starts from `i + 1`, and `right` starts from the end of the array. Here, `i` represents the current index of the element `n`.
2) Check if the sum of the numbers pointed to by these two pointers is equal to 0
    - If it is equal, add them to the triplets array
        - Skip if the next `num[left]` is equal to the previous one by increment `left` by 1
        - Skip if the next `num[right]` is equal to the previous one by decrement `right` by 1
    - If it is too large, decrement the right pointer by 1
    - Otherwise, increment the left pointer by 1 since it is too small
3) Return ans

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


- Time Complexity: O(N^2)
- Space Complexity: O(N)
