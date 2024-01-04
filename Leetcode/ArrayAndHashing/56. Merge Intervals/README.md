## 56. Merge Intervals
🔗  Link: [Merge Intervals](https://leetcode.com/problems/merge-intervals/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, Sorting<br>

=======================================================================================<br>
Given an array of intervals where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.


Example 1:<br>
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]<br>
Output: [[1,6],[8,10],[15,18]]<br>
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].<br>


Example 2:<br>
Input: intervals = [[1,4],[4,5]]<br>
Output: [[1,5]]<br>
Explanation: Intervals [1,4] and [4,5] are considered overlapping.<br>

Example 3:<br>
Input: intervals = [[1,5]]<br>
Output: [[1,5]]<br>

Constraints:<br>
- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti <= endi <= 10^4


=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input array be empty?
    - No, the minimum interval length is 1
2. Any requirement on time/space complexity?
    - O(nlogn) time and O(1) space not including the resulting output array
3. Is the array sorted?
    - No the intervals are not guaranteed to be sorted order
 
### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. Sort <br>
Sorting the intervals by their start times ensures that you process them in a sequential order. This is essential because it allows you to easily compare each interval with the previous one to check for overlaps. With sorted intervals, the logic to merge them becomes straightforward. If intervals are not sorted, we would have to compare each interval with all previously processed intervals, significantly complicating the algorithm and increasing its time complexity.

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: sort the intervals first and then efficiently merge overlapping intervals in a single pass. We only need to compare each interval with the last one in our result list. 

1) Sort all intervals based on their low endpoints
2) Initialize the results with the first interval
3) Iterate through each interval:
    1) Compare the high endpoint of the last interval in the results with the low endpoint of the current interval
    2) If the high endpoint of the last interval is greater than or equal to the low endpoint of the current interval, update the high endpoint of the last interval in the results to be the maximum of the current high and the last high
    3) Otherwise, add the current interval to the results as it does not overlap with the previous one.
4) Return the merged intervals in the results

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the number of intervals

- Time Complexity: O(NlogN)
- Space Complexity: O(1), not including the output array 
