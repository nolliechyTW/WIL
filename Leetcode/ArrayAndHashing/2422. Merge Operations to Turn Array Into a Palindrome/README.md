## 2422. Merge Operations to Turn Array Into a Palindrome
🔗  Link: [Merge Operations to Turn Array Into a Palindrome](https://leetcode.com/problems/merge-operations-to-turn-array-into-a-palindrome/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, Two pointers, Greedy<br>

=======================================================================================<br>
You are given an array `nums` consisting of positive integers.<br>
You can perform the following operation on the array any number of times:<br>
- Choose any two adjacent elements and replace them with their sum.
    - For example, if `nums = [1,2,3,1]`, you can apply one operation to make it `[1,5,1]`.
Return the minimum number of operations needed to turn the array into a palindrome.


Example 1:<br>
Input: nums = [4,3,2,1,2,3,1]<br>
Output: 2<br>
Explanation: We can turn the array into a palindrome in 2 operations as follows:
- Apply the operation on the fourth and fifth element of the array, nums becomes equal to [4,3,2,**3**,3,1].
- Apply the operation on the fifth and sixth element of the array, nums becomes equal to [4,3,2,3,**4**].
The array [4,3,2,3,4] is a palindrome.<br>
It can be shown that 2 is the minimum number of operations needed.<br>

Example 2:<br>
Input: nums = [1,2,3,4]<br>
Output: 3<br>
Explanation: We do the operation 3 times in any position, we obtain the array [10] at the end which is a palindrome.<br>

Constraints:<br>
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^6
=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input array be empty?
2. Any requirement on time/space complexity?
3. How should the function handle edge cases like an empty array or an array with a single element?

 
### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. Two Pointers
The goal is to make all elements in the array equal, which often involves symmetric operations from both ends of the array. Two pointers, starting from opposite ends, allow for an efficient comparison and modification of elements in a balanced way.

2. Greedy
The algorithm's greedy nature lies in its focus on making the best immediate choice at each step, aiming for quick and local optimization without considering the global implications of these choices. 


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: uses a two-pointer approach, moving inward from both ends of the array, and at each step, it merges the smaller pair of adjacent elements, counting each merge as an operation.


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
