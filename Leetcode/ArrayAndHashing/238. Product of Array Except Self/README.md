## 238. Product of Array Except Self
🔗  Link: [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, Presum<br>

=======================================================================================<br>
Given an integer array nums, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

You must write an algorithm that runs in `O(n)` time and without using the division operation.


Example 1:<br>
Input: nums = [1,2,3,4]<br>
Output: [24,12,8,6]<br>

Example 2:<br>
Input: nums = [-1,1,0,-3,3]<br>
Output: [0,0,9,0,0]<br>

Constraints:<br>
- 2 <= nums.length <= 105<br>
- -30 <= nums[i] <= 30<br>
- The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.
=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input array be empty? 
    - The minimum input has two numbers
2. Any requirement on time/space complexity? 
    - Solve in O(1) extra space complexity

    EDGE CASE<br>
    Input: nums = [-3,3]<br>
    Output: [3,-3]<br>


### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. Left and Right product lists / Pointers <br>
We can create two lists: one to store the product of all numbers to the left of each element and another to store the product of all numbers to the right of each element. By multiplying the corresponding elements from these two lists, we can compute the desired result.



### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use two pointer from both ends of the array to generate the product from both sides of each number to achieve the product except self.


1) Create product from the left side of each num and store left_product in it
2) Create product from the right side of each num and store right_product in it
3) Create a `result` list by iterating through each element of the input nums list 
    - For each element at index i, calculate its corresponding product by multiplying the values at the same index in the left_products and right_products lists
    -  Store this product in the result list. 
4) Finally, return the result list, which contains the product of all numbers except the number at the current position

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
