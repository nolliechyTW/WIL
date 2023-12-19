## 1492. The kth Factor of n
🔗  Link: [The kth Factor of n](https://leetcode.com/problems/the-kth-factor-of-n/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Number Thoery, Math<br>

=======================================================================================<br>
You are given two positive integers `n` and `k`. A factor of an integer `n` is defined as an integer `i` where `n` % `i` == 0.

Consider a list of all factors of `n` sorted in ascending order, return the `kth` factor in this list or return `-1` if `n` has less than `k` factors.

Example 1:<br>
Input: n = 12, k = 3<br>
Output: 3<br>
Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3<br>

Example 2:<br>
Input: n = 7, k = 2<br>
Output: 7<br>
Explanation: Factors list is [1, 7], the 2nd factor is 7<br>

Example 3:<br>
Input: n = 4, k = 4<br>
Output: -1<br>
Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1<br>

Constraints:<br>
1 <= k <= n <= 1000<br>
=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. If n is a perfect square, should the repeated factor (the square root of n) be counted once or twice?
    - only count once
2. Any requirement on time/space complexity?
    - Could you solve this problem in less than O(n) complexity?

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. Number Thoery<br>
The factors of n will be always in the range [1, n].

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Keep a list of all factors sorted. Loop factor from 1 to n and add it to factors array if n % factors == 0. Return the kth factor if it exist else return -1.

OPTIMAL:


### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N is the positive integers n.
- Time Complexity: O(N)
- Space Complexity: O(N)
