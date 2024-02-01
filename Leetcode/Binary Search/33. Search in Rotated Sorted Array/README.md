## 33. Search in Rotated Sorted Array
🔗  Link: [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, Binary Search<br>

=======================================================================================<br>
There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k` (1 <= k < nums.length) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (0-indexed). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.

Given the array `nums` after the possible rotation and an integer `target`, return *the index of target* if it is in nums, or `-1` if it is not in nums.


Example 1:<br>
Input: nums = [4,5,6,7,0,1,2], target = 0<br>
Output: 4<br>

Example 2:<br>
Input: nums = [4,5,6,7,0,1,2], target = 3<br>
Output: -1<br>

Example 3:<br>
Input: nums = [1], target = 0<br>
Output: -1<br>


Constraints:<br>
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- All values of nums are unique.
- nums is an ascending array that is possibly rotated.
- -10^4 <= target <= 10^4

=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input array be empty? 
    - We don’t need to consider empty inputs
2. Any requirement on time/space complexity? 
    - You must write an algorithm with O(log n) runtime complexity.
3. Will there be negative numbers?
    - Yes, the number will be both negative and positive

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Binary Search<br>
Binary search is typically used when the data is sorted or partially sorted. In this problem, we are dealing with a rotated sorted array, which is a variant of a sorted array. This is a strong indicator that binary search might be a suitable approach. Also, binary search is chosen for its efficiency in searching. It has a time complexity of O(log n), making it much faster than linear search (O(n)) 

2. Two pointers <br>
The two-pointer technique is inherent in binary search, where you typically have `left` and `right` pointers. In problems we you need to narrow down a range (like finding a target in a sorted array), using two pointers to adjust the search space is a natural approach.


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

- General Idea: differentiate between the sorted and unsorted halves of the array at each step, adjusting the search boundaries to efficiently locate the target value

1) Initialize Pointers: Set `left` and `right` pointers to the start and end of the array, respectively

2) Start Binary Search Loop: Begin a while loop that continues as long as `left` is **less than or equal to** `right`

3) Calculate Middle Index: Inside the loop, calculate the `mid` index. This is done by averaging `left` and `right`, which helps in dividing the array into two halves for the binary search

4) Check for Target at Mid: If the element at `mid` is the target, return `mid` as the found index

5) Identify Sorted Half:

    - If the left half of the array (from `left` to `mid`) is sorted:
        - Check if the target is within this sorted left half. If yes, adjust the `right` pointer to `mid - 1` to focus the next search in this half
        - Otherwise, adjust the `left` pointer to `mid + 1` to search in the right half

    - If the left half is not sorted, then the right half must be sorted:
        - Check if the target is within the sorted right half. If yes, adjust the `left` pointer to `mid + 1`
        - Otherwise, adjust the `right` pointer to `mid - 1` to search in the left half

6) Target Not Found: If the loop ends without returning, it means the target is not in the array. Return `-1` in this case


### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N be the length of `nums`

- Time Complexity: O(logN), binary search
- Space Complexity: O(1)
