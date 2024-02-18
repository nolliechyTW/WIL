## 523. Continuous Subarray Sum
🔗  Link: [Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, Hashmap, Prefix Sum<br>

=======================================================================================<br>
Given an integer array nums and an integer `k`, return `true` if nums has a good subarray or `false` otherwise.<br>

A good subarray is a subarray where:<br>
- its length is **at least two**, and
- the sum of the elements of the subarray is a multiple of `k`.


Note that:<br>
- A subarray is a contiguous part of the array.
- An integer `x` is a multiple of `k` if there exists an integer `n` such that `x = n * k`. 
- `0` is always a multiple of `k`.<br>


Example 1:<br>
Input: nums = [23,2,4,6,7], k = 6<br>
Output: true<br>
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.<br>

Example 2:<br>
Input: nums = [23,2,6,4,7], k = 6<br>
Output: true<br>
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.<br>
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.<br>


Example 3:<br>
Input: nums = [23,2,6,4,7], k = 13<br>
Output: false<br>


Constraints:<br>
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
- 0 <= sum(nums[i]) <= 2^31 - 1
- 1 <= k <= 2^31 - 1

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
3. Can the divisor k be zero, negative, or only positive?
- Only positive
4. Is there negative interger in the array?
- Only positive

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1) Hashmap:
- The key operation here is taking the modulus of the cumulative sum by `k`. This operation reduces the range of possible values, making direct comparisons meaningful for solving the problem. The goal is to find two indices `i` and `j` where the cumulative sums at these indices, say `sum[i]` and `sum[j]`, when taken modulus `k`, yield the same remainder. This implies that the sum of elements between `i + 1` and `j` is a multiple of `k`. 
- Using a hashmap allows for constant-time lookups to check if a particular modulus result has occurred before.



### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: 


1) Initialization:
- Create a hashmap to store the **first occurrence of cumulative sums modulo k**. 
- Initialize this hashmap with `{0: -1}` to handle cases where a valid subarray starts from the beginning.
- Initialize a variable to keep track of the current cumulative sum.

2) Iterate Through the Array:
- For each element in the array, add the element's value to the current cumulative sum.
- If *k is not zero*, apply the modulus operation to the current cumulative sum with k to obtain the remainder. This step ensures that we are always working with the remainder of the cumulative sum divided by k, which is critical for finding subarrays whose sums are multiples of k.

3) Check for Previously Seen Remainders:
- **For each cumulative sum's remainder (after applying modulus k), check if this remainder has been seen before in the hashmap**.
    - If the remainder has been seen before, calculate the length of the potential subarray by subtracting the current index `i` from the stored index of the first occurrence of this remainder. If the length is greater than 1, it means we have found a contiguous subarray whose sum is a multiple of `k`, and we return `True`.
    - If the remainder has not been seen before, **store** the current index `i` in the hashmap with the remainder as the key. This step records the first occurrence of each possible remainder.

4) Return False:
If the loop completes without finding any qualifying subarray, return `False`, indicating that no such subarray exists in the given array.

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
- Space Complexity: O(N)
  