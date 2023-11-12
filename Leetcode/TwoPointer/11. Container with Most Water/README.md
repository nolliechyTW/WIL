## 11. Container With Most Water
🔗  Link: [Container With Most Water](https://leetcode.com/problems/container-with-most-water/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Two Pointers, Array<br>

=======================================================================================<br>
Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

Example 1:
[img](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png) <br>
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]<br>
Output: 6<br>
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.<br>

Example 2:<br>
Input: height = [4,2,0,3,2,5]<br>
Output: 9<br>


Constraints:<br>
n == height.length<br>
1 <= n <= 2 * 10^4<br>
0 <= height[i] <= 10^5<br>
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

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1.  Loop twice<br>
Use to loop to find the maximum area. It works but exceed time limit lol
2. Pointers <br>
Use two pointers, one from the left the other from the right. 

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Begin by calculating the area formed by the outermost lines. To maximize it, we move the pointer of the shorter line inward. While this reduces width, the potential increase in height could surpass the width reduction, enhancing the overall area.
1) Initialize variable `maxArea` to keep track of max area 
2) Initialize two pointers, `left` and `right`, where `left` starts from `0`, and `right` starts from the end of the array
2) Calculate and keep track of the maximum area of the container
    - If left line is shorter, move `left` by 1 
    - If right line is shorter, move `right` by 1 
    - Stop when left equal/exceed right
3) Return `maxArea`

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
