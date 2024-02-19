## 560. Subarray Sum Equals K
🔗  Link: [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, Hashmap, Prefix Sum<br>

=======================================================================================<br>
Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:<br>
Input: nums = [1,1,1], k = 2<br>
Output: 2<br>

Example 2:<br>
Input: nums = [1,2,3], k = 3<br>
Output: 2<br>

Constraints:<br>
- 1 <= nums.length <= 2 * 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7

=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the    are aligned on the expected inputs and outputs.
1. Can the input be empty?
- No, assume there is at least one integer in the string
2. Any requirement on time/space complexity?
- O(N) in time
3. Are there any restrictions on the use of additional data structures?
-  No
4. Is there negative interger in the array?
- Yes!!

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

- PrefixSum:<br>
1) A prefix sum is a running total of the sums of elements in an array up to a certain index. For any array nums, the prefix sum up to index `i` is the sum of all elements from `nums[0]` to `nums[i]`. This concept is crucial because it allows for the calculation of the sum of any subarray in constant time, given the prefix sums

- Hashmap<br>
1) As we calculate prefix sums while iterating through the array, we can store each prefix sum in a hashmap. **The key in this hashmap is the prefix sum value, and the value is the frequency of that prefix sum occurring up to the current point in the iteration**
2) To find a subarray that sums to `k`, we look for situations where `currentPrefixSum - k` is a prefix sum that has occurred before. **If `currentPrefixSum - k` exists in our hashmap, it means there is a previous point in the array where the sum of all elements up to that point is `currentPrefixSum - k`.** The subarray between that point and the current index sums to k



### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: 


1) Initialization: 
- We start with a hashmap that initially contains the entry {0: 1} to indicate that there is one occurrence of a zero sum before any elements are processed. This accounts for cases where a prefix sum equals k from the start of the array

2) Iteration and Updating: 
- As we iterate through the array, we update the current prefix sum and check if `currentPrefixSum - k` exists in the hashmap. 
    - If it does, we add its frequency to the result. This step directly uses the hashmap to find the number of preceding subarrays that, when added to the current segment, sum to k

3) HashMap Update: 
- After checking for `currentPrefixSum - k`, we update the hashmap with the current prefix sum, either by initializing its frequency to 1 if it's not already present or incrementing its existing frequency
-  This update step is crucial for ensuring that all subsequent elements can check against all possible prefix sums seen so far

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the number of integer in the array `nums`.


- Time Complexity: O(N)
- Space Complexity: O(1)
  