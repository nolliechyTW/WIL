## 239. Sliding Window Maximum
🔗  Link: [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/description/)<br>
💡 Difficulty: Hard<br>
🛠️ Topics: Array, Sliding Window, Queue<br>

=======================================================================================<br>
You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 
Example 1:<br>

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3<br>
Output: [3,3,5,5,6,7]<br>
Explanation: <br>
Window position                 Max <br>
-----------------                 --- <br>
[1  3  -1] -3  5  3  6  7       3<br>
 1 [3  -1  -3] 5  3  6  7       3<br>
 1  3 [-1  -3  5] 3  6  7       5<br>
 1  3  -1 [-3  5  3] 6  7       5<br>
 1  3  -1  -3 [5  3  6] 7       6<br>
 1  3  -1  -3  5 [3  6  7]      7<br>


Example 2:<br>
Input: nums = [1], k = 1<br>
Output: [1]<br>


Constraints:<br>
1 <= nums.length <= 10^5<br>
-10^4 <= nums[i] <= 10^4<br>
1 <= k <= nums.length<br>
=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input array be empty?
    - No, we assume that nums always contains at least one element
2. Any requirement on time/space complexity? 
    - O(n) in time
3. Is it possible the length of `nums` is shorter than `k`?
    - No


### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. Sliding Window<br>
In this problem, the sliding window technique is used to explore and iterate through an input list `nums` of integers with a specified window size `k`. The goal is to find the maximum value within each sliding window as it moves through the array. 

2. Queue<br>
We can use a **monotonic queue** as it supports efficient insertion, deletion, and retrieval of elements from the ends of a window. We will implement it with the `deque` data structure.




### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea:  Using a deque (q) to maintain indices in decreasing order based on their corresponding values in the nums array. This ensures that the front of the deque always holds the index of the maximum element within the current sliding window. The reason we need to store the indices instead of the elements themselves is that we need to detect when elements leave the window due to sliding too far to the right.

1) Initialize an empty list `res` to store the results
2) Initialize a deque `q` to save indices
3) Initialize `left` and `right` pointers to 0
4) Iterate through the elements of the input list nums using the right pointer until it reaches the end of the list
    - While the deque `q` is not empty and the current element at right index is greater than the element at the index stored in `q[-1]`, pop elements from the back of the deque
    - Append the current right index to the deque q
    - If the index at the front of the deque q is less than left, pop elements from the front of the deque, as they are no longer in the current window
    - If the current window size `(right + 1)` is greater than or equal to k, append the element at the index stored in q[0] since it's the maximum element in the current window to the result and adjust the pointer correspondingly

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume `N` is the length of input array.

- Time Complexity: O(N)
- Space Complexity: O(k)