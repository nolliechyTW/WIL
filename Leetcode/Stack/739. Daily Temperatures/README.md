## 739. Daily Temperatures
🔗  Link: [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, Stack<br>

=======================================================================================<br>
Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer`[i] == 0 `instead.


Example 1:<br>
Input: temperatures = [73,74,75,71,69,72,76,73]<br>
Output: [1,1,4,2,1,1,0,0]<br>

Example 2:<br>
Input: temperatures = [30,40,50,60]<br>
Output: [1,1,1,0]<br>

Example 3:<br>
Input: temperatures = [30,60,90]<br>
Output: [1,1,0]<br>


Constraints:<br>
- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100


=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1) Regarding the definition of a 'warmer temperature,' should we consider a day as warmer only if the temperature on a future day is strictly higher than the current day, or is it acceptable if the future temperature is equal to the current day?
2) Any requirement on time/space complexity?
    - Shoule be O(N) for both time complexity and space complexity

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Stack <br>
Using a stack is a common and efficient approach to solve problems that involve finding the next greater element or the next smaller element for elements in an array.<br>
    -  By maintaining a monotonic decreasing stack, we can keep track of the indices of elements in the array in a way that ensures the stack contains elements in descending order of temperatures
    - When encountering a new element in the array, we can efficiently compare its temperature with the temperatures of elements represented by the indices in the stack
    -  Using a stack allows us to process each element in the array only once, making the algorithm more efficient compared to nested loops


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Utilize a stack to track array indices while maintaining a monotonic decreasing order of temperatures. During array traversal, compare the current temperature with the stack's top. If higher, update the result array with the time difference between the current day and the popped index.

1) Initialize an empty stack to store indices of temperatures
2) Initialize the result array with zeros
3) Iterate through the temperatures array
    - While the stack is not empty and the current temperature is higher than the temperature represented by the top of the stack, pop the index from the stack and update the result array with the difference in days
4) Push the current index onto the stack
5) After iteration, since the remaining indices in the stack have no warmer temperatures, they remain with 0 in the result array
6) Return the result array

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N be the total number of elements in array.

- Time Complexity: O(N)
- Space Complexity: O(N)
