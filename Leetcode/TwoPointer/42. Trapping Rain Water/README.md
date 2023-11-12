## 42. Trapping Rain Water
🔗  Link: [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/description/)<br>
💡 Difficulty: Hard<br>
🛠️ Topics: Two Pointers, Array<br>

=======================================================================================<br>
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:<br>
Input: height = [1,8,6,2,5,4,8,3,7]<br>
Output: 49<br>
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.<br>

Example 2:<br>
Input: height = [1,1]<br>
Output: 1<br>

Constraints:<br>
n == height.length<br>
2 <= n <= 10^5<br>
0 <= height[i] <= 10^4<br>
=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input array be empty? 
    - Yes
2. Any requirement on time/space complexity? 
3. Is the input array sorted?
    - No

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1.  Pointers <br>
Use two pointers, one from the left the other from the right and then we can efficiently compute the trapped rainwater by iterating from both ends towards the peak height.

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Begin by initializing pointers at the start and end of the array. Calculate the potential trapped water between these two pointers and the peak height. 

1) Find the index of the tallest bar
2) Loop through the Left Side
    - Update `left_max`: At each step, `left_max` is updated to the maximum of its current value and the height of the current bar, ensuring it represents the maximum height encountered on the left.
    - Calculate Trapped Water: The trapped water on the left side is determined by the positive difference between `left_max` and the height of the current bar. The maximum of this difference and 0 is added to the rainfall accumulator, representing the potential for water to be trapped.
3) Loop through the Right Side
4) Return the total trapped water

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
