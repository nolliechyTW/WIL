## 4. Median of Two Sorted Arrays
🔗  Link: [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/description/)<br>
💡 Difficulty: Hard<br>
🛠️ Topics: Array, Binary Search<br>

=======================================================================================<br>
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

 

Example 1:<br>
Input: nums1 = [1,3], nums2 = [2]<br>
Output: 2.00000<br>
Explanation: merged array = [1,2,3] and median is 2.<br>

Example 2:<br>
Input: nums1 = [1,2], nums2 = [3,4]<br>
Output: 2.50000<br>
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.<br>


Constraints:<br>
- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -10^6 <= nums1[i], nums2[i] <= 10^6

=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input array be empty? 
    - We don’t need to consider empty inputs
2. Any requirement on time/space complexity? 
    - You must write a solution in O(log(m * n)) time complexity and O(1) space complexity


### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. Binary Search <br>
Binary search is a method for locating an element in a sorted list efficiently. Searching for an element can be done naively in O(N) time, but binary search speeds it up to O(log N).


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

- General Idea: utilizes binary search to find a partition point in the shorter array, ensuring that the elements on both sides of the partition create a valid median for the combined arrays
1) Variable Initialization:
- Determine the lengths len_nums1 and len_nums2 of the input arrays nums1 and nums2.
- Ensure that nums1 is the shorter array. If not, swap nums1 and nums2.

2) Calculate Total Length and Midpoint:
- Calculate the total length total_len of the combined arrays.
- Compute the midpoint mid_point as half of the total length rounded up.

3) Binary Search:
- Initialize two pointers low and high for binary search in the shorter array nums1.
- While low is less than or equal to high, perform binary search:
    - Compute the midpoints mid1 and mid2 based on the current values of low and high.
    - Calculate the values l1, l2, r1, and r2 representing elements around the potential partition.

4) Check Valid Partition:
- Check if the current partition is valid by ensuring that l1 <= r2 and l2 <= r1.

5) Determine Median:
- If the partition is valid:
    - If the total length is odd, return the maximum of l1 and l2 as the median.
    - If the total length is even, return the average of the maximum of l1 and l2 and the minimum of r1 and r2 as the median.

6) Adjust Pointers:
- If l1 > r2, adjust high for the binary search.
- If l2 > r1, adjust low for the binary search.

7) Repeat Binary Search:
- Repeat the binary search until a valid partition is found or low exceeds high.

8) Default Case:
- If no valid partition is found, return 0.0 as the default median.


### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` 

- Time Complexity: O(log (m+n))
- Space Complexity: O(1)
