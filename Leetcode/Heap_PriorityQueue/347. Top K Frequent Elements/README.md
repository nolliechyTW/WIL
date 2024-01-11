## 347. Top K Frequent Elements
🔗  Link: [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, Hashmap, Heap<br>

=======================================================================================<br>
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.<br>

Example 1:<br>
Input: nums = [1,1,1,2,2,3], k = 2<br>
Output: [1,2]<br>

Example 2:<br>
Input: nums = [1], k = 1<br>
Output: [1]<br>


Constraints:<br>
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k is in the range `[1, the number of unique elements in the array]`
- It is guaranteed that the answer is unique

=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Will k be smaller or equal to the length of nums? 
    - Yes
2. Any requirement on time/space complexity? 
    - time complexity must be better than O(n log n), where n is the array's size
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

- General Idea: The min heap essentially keeps track of the k most frequent elements seen so far. By maintaining a size of k, it ensures that less frequent elements are discarded, and only the k most frequent elements remain. When the iteration is complete, we extract elements from the heap, which are our k most frequent elements

1) Count Frequencies: 
First, we iterate through the array and use a hash map to count the frequency of each element.

2) Use a Heap to Keep Track of k Most Frequent Elements: 
We can use a min-heap to keep track of the k most frequent elements. The key here is to maintain the size of the heap to k. If the size of the heap exceeds k, we pop the least frequent element.

3) Extract k Most Frequent Elements: 
Finally, we extract elements from the heap, which are our k most frequent elements.

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the number of items in the array `nums`

- Time Complexity: O(N log k) since inserting elements into the heap takes O(log k) time for each of the N elements
- Space Complexity: O(N) for storing the frequency map, and O(k) for the heap, resulting in O(N + k). In the worst case, this can be O(N)