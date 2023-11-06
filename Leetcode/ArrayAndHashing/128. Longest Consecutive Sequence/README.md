## 128. Longest Consecutive Sequence
🔗  Link: [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, Hash<br>

=======================================================================================<br>
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

Example 1:<br>
Input: nums = [100,4,200,1,3,2]<br>
Output: 4<br>
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.<br>

Example 2:<br>
Input: nums = [0,3,7,2,5,8,4,6,0,1]<br>
Output: 9<br>

Constraints:<br>
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input array be empty?
    - yes
2. Any requirement on time/space complexity?
    - You must write an algorithm that runs in O(n) time
3. What should we return if there is no subsequence with consecutive elements?
    - return 0
4. What should I return for an empty array?
    - return 0
5. What should we return if there are duplicate elements in the subsequence?
    - Duplicates don't add to the count
### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. Sort <br>
We can sort the array of numbers and check if the next item is equal to the prev item add 1. Once we find a match, we keep track of the length of consecutive sequence and return the longest. This works but the time complexity will be O(nlogn)
2. Storing the elements of the array in a HashSet<br>
As we iterate through the array, we can store each number in a HashSet instantly remove duplicates from our list

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use a hash set to find the longest length

1) Keep track of longestStreak starting at 0.
2) Create a hashset 
3) Loop through the number set
    - If current number has no previous number, then start counting from this number
    - Else if  the set contains currentNum + 1, increment currentNum and currentStreak
4) After each while loop, check and set longestStreak
5) Return longestStreak


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
