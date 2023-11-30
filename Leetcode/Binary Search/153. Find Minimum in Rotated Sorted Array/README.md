## 153. Find Minimum in Rotated Sorted Array
🔗  Link: [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, Binary Search<br>

=======================================================================================<br>
Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:
- `[4,5,6,7,0,1,2]` if it was rotated `4` times.
- `[0,1,2,4,5,6,7]` if it was rotated `7` times.
Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

Example 1:<br>
Input: nums = [3,4,5,1,2]<br>
Output: 1<br>
Explanation: The original array was [1,2,3,4,5] rotated 3 times.<br>

Example 2:<br>
Input: nums = [4,5,6,7,0,1,2]<br>
Output: 0<br>
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.<br>

Example 3:<br>
Input: nums = [11,13,15,17]<br>
Output: 11<br>
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.<br>

=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input array be empty? 
2. Are rotations always performed in a specific direction, such as clockwise or counterclockwise?
    - Yes, always clockwise
3. Any requirement on time/space complexity? 
    - You must write an algorithm that runs in O(log n) time


### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. Binary Search <br>
Binary search is a method for locating an element in a sorted list efficiently. Searching for an element can be done naively in O(N) time, but binary search speeds it up to O(log N). Since the given array is sorted, we can make use of binary search. However, the array is rotated. So simply applying the binary search won't work here.


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

- General Idea: The goal is to identify the **inflection point**, which is the point where the order of elements changes – all elements to the left are greater than the first element, and all elements to the right are less than the first element.<br>
1) Find the mid element of the array:
- If `nums[mid] > nums[right]`, it implies that the inflection point is on the right side of mid, so update `left = mid + 1`
- Otherwise, if `nums[mid] <= nums[right]`, it implies that the inflection point is on the left side or at mid. Update `right = mid`.

2) Stop our search when we find the inflection point and return the result. 

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


- Time Complexity: O(logN)
- Space Complexity: O(1)
