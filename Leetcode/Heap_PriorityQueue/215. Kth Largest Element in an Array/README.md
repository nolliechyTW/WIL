## 215. Kth Largest Element in an Array
🔗  Link: [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, Heap, Divide and Conquer, Quickselect<br>

=======================================================================================<br>
Given an integer array `nums` and an integer `k`, return the `kth` largest element in the array.

Note that it is the `kth` largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
 

Example 1:<br>
Input: nums = [3,2,1,5,6,4], k = 2<br>
Output: 5<br>

Example 2:<br>
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4<br>
Output: 4<br>


Constraints:<br>
- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Will k be smaller or equal to the length of nums? 
    - Yes
2. Any requirement on time/space complexity? 
    - You must write a solution in O(n) time complexity and O(n) space complexity
3. Should we assume the array is unsorted to begin with?
    - Yes


### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. Heap <br>
The core task of finding the kth largest (or smallest) element in a collection is a classic example of an **order statistics** problem. Heaps are particularly well-suited for these problems because they can efficiently maintain order properties.<br>
A heap is particularly useful *when you don’t need the entire array sorted*. If you're only interested in a subset of the sorted elements (like the kth largest), a heap efficiently provides access to these elements without the overhead of fully sorting the data.

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

- General Idea: The min heap essentially keeps track of the k largest elements seen so far. By **maintaining a size of k**, it ensures that smaller elements are discarded, and only the k largest elements remain. When the iteration is complete, the smallest among these k largest elements (which is at the root of the min heap) is the kth largest element in the array

1) Initialize a Min Heap:
    - Create an empty min heap called `heap`.
2) Iterate through the Array:
    - Loop through each number (`num`) in the `nums` array.
3) Build and Maintain the Heap:
    - Add `num` to the heap using `heapq.heappush()`.
    - Check if the heap size exceeds `k`. If it does, remove the smallest element (heap root) using `heapq.heappop()`. This ensures the heap always contains the `k` largest elements seen so far.
4) Return the kth Largest Element:
    - After processing all elements in `nums`, the root of the heap (`heap[0]`) is the kth largest element, as **it is the smallest among the k largest elements in the array**.

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the number of items in the array

- Time Complexity: O(N log N)
- Space Complexity: O(N) because we need to generate and store a heap.

<!-- 

To analyze the time complexity of the provided code, let's break down the operations:

1) Heap Construction (Heap Push):
- The code iterates through all N elements in the array nums.
- For each element, it performs a heapq.heappush() operation. This operation has a time complexity of O(log n) for each push, where n is the number of elements currently in the heap.
- As the heap grows with each iteration, the time complexity of building the heap in this way is O(N log N), where N is the total number of elements in nums.

2) Finding the kth Largest Element (Heap Pop):
- The code then pops elements from the heap k times.
- Each heapq.heappop() operation has a time complexity of O(log n), where n is the number of elements currently in the heap.
- Since the heap size decreases with each pop, the worst-case time complexity for all k pops is O(k log N).

Combining these two parts, the overall time complexity of the function is O(N log N + k log N). However, since in the worst case k can be as large as N (if we are asked to find the largest element), the time complexity simplifies to O(N log N), which is the dominant term.
 -->