## 78. Subsets
🔗  Link: [Subsets](https://leetcode.com/problems/subsets/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, Backtracking<br>

=======================================================================================<br>
Given an integer array `nums` of unique elements, return all possible subsets(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.<br>

Example 1:<br>
Input: nums = [1,2,3]<br>
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]<br>

Example 2:<br>
Input: nums = [0]<br>
Output: [[],[0]]<br>

Constraints:<br>
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of `nums` are unique

=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input array be empty? What should I return for an empty string?
    - Conventionally, the power set of an empty set includes just the empty set itself
2. Any requirement on time/space complexity?
3. What is the range of the size of the input array nums? Is there a maximum number of elements that nums can have?
4. Is the input array assumed to be always sorted?
    - No, do not assume array is always sorted.


### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. Backtracking <br>
Whenever we have a problem where we need to generate all combinations/permutations of some group of letters/numbers, the first thought we should have is backtracking. Backtracking algorithms can often keep the space complexity linear with the input size.
The strategy accepts the cases which satisfy conditions and reject the others. We basically loop over every element in our input nums, and we recursively call the method to generate subsets corresponding to that element in the next line and then we remove that element since we are done with it, and we add it to our subsets array.

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: use a recursive backtracking function, named `backtrack`, to build subsets incrementally. The function backtrack takes two parameters: `start`, which represents the current index in the array nums, and `path`, which is the current subset being formed. The method begins with an empty subset and explores all possible elements to be included in the current subset.

1) Initialize an Empty Result List: The method `subsets` initializes an empty list `res` to store all subsets. Initially, `res` is set to `[]`.

2) Recursive Backtracking Function: The `backtrack` function is defined within subsets. It iterates over the elements of the array nums, starting from the index `start`.

3) Building Subsets Incrementally:
    - For each index `i` in the range from `start` to the `end of the array`, the element `nums[i]` is appended to the current subset `path`.
    - After adding `nums[i]` to `path`, a copy of path is appended to `res`, capturing the current state of the subset.
    - The function then makes a recursive call to backtrack with the next index `(i + 1)`, allowing for further exploration.

4) Backtracking to Explore Other Possibilities:
    - After the recursive call, `path.pop()` is executed, which removes the last element added to path. This step is crucial as it undoes the last addition, allowing the function to backtrack and explore other subset combinations by including different elements in subsequent iterations.

5) Complete Exploration: The process continues until the function has iterated through all elements in `nums`, effectively considering every possible combination of elements for inclusion in the subsets.

6) Returning the Result: Once all recursive calls are complete and all possible subsets have been explored and added to `res`, the subsets method returns `res`, which now contains every possible subset of the input array `nums`.

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N is the number of elements in the input array.

- Time Complexity: O(2^N), at each step, the algorithm explores two possibilities for each element – either including it in the current subset or not.
- Space Complexity: O(N), where N represents the maximum depth of the recursion stack if we exclude the space required for the output list
