## 217. Contains Duplicate
🔗  Link: [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/description/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: Array, Sort, Hash<br>

===========================================================<br>
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:<br>
Input: nums = [1,2,3,1]<br>
Output: true<br>

Example 2:<br>
Input: nums = [1,2,3,4]<br>
Output: false<br>

Example 3:<br>
Input: nums = [1,1,1,3,3,4,3,2,4,2]<br>
Output: true<br>

Constraints:<br>
1 <= nums.length <= 105<br>
-109 <= nums[i] <= 109<br> 
===========================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input array be empty?
2. Any requirement on time/space complexity?
3. Is the array sorted?

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. Sort <br>
We can sort the array of numbers and check if the next item is equal to the prev item. Once we find a match, we can return True. Otherwise we reach the end of the array and return False.
2. Storing the elements of the array in a HashMap or a Set<br>
As we iterate through the array, we can store each number in a Set. If the number is already in the Set, then we can return True. Otherwise we reach the end of the array and return False.

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Create a Set to store number. If the number is already in the Set, then return True. Otherwise we reach the end of the array and return False.

1) Create Set
2) Iterate through numbers
    - If number is already in set return True
    - Else store number in set
3) Return False if we have reached the end of the list without duplicate


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
