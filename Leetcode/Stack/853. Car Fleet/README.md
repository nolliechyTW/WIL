## 853. Car Fleet
🔗  Link: [Car Fleet](https://leetcode.com/problems/car-fleet/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, Stack<br>

=======================================================================================<br>
There are `n` cars going to the same destination along a one-lane road. The destination is `target` miles away.

You are given two integer array `position` and `speed`, both of length `n`, where `position[i]` is the position of the `ith` car and `speed[i]` is the speed of the `ith` car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.

 

Example 1:<br>
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]<br>
Output: 3<br>
Explanation:<br>
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.<br>
The car starting at 0 does not catch up to any other car, so it is a fleet by itself.<br>
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.<br>
Note that no other cars meet these fleets before the destination, so the answer is 3.<br>

Example 2:<br>
Input: target = 10, position = [3], speed = [3]<br>
Output: 1<br>
Explanation: There is only one car, hence there is only one fleet.<br>

Example 3:<br>
Input: target = 100, position = [0,2,4], speed = [4,2,1]<br>
Output: 1<br>
Explanation:<br>
The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The fleet moves at speed 2.<br>
Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.<br>


Constraints:<br>
- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100
- n == position.length == speed.length
- 1 <= n <= 10^5
- 0 < target <= 10^6
- 0 <= position[i] < target
- All the values of position are unique.
- 0 < speed[i] <= 10^6

=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1) Can a car join an existing car fleet if it catches up to it?
    - Yes
2) Any requirement on time/space complexity?
    - Should be O(N) for both time complexity and space complexity

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Stack <br>
Using a stack to keep track of the time it takes for each car to reach the destination and to determine whether a car can form a new fleet or join an existing fleet.


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Utilize a stack to track array indices while maintaining a monotonic decreasing order of temperatures. During array traversal, compare the current temperature with the stack's top. If higher, update the result array with the time difference between the current day and the popped index.

1) Create a list of pairs, where each pair consists of a car's initial position (position) and its speed (speed)
2) Sort the list of pairs in descending order based on the initial positions. This is done to process cars starting from the back of the road first
3) Initialize an empty stack to keep track of the time it takes for each car to reach the target position
4) Iterate through the sorted list of pairs. For each car:
    - Calculate the time it will take to reach the target position using the formula (target - position) / speed
    - Push this time onto the stack
    - Check if there are at least two cars in the stack (since a fleet requires at least two cars)
    - If the time taken by the current car is less than or equal to the time taken by the car ahead of it (top of the stack), it means they will form a fleet
    - If they will form a fleet, pop the top car from the stack
    - After processing all the cars, the length of the stack will give you the number of car fleets formed

5) Return the length of the stack as the result

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

- Time Complexity: O(Nlog(N))
- Space Complexity: O(N)
