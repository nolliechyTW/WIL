## 875. Koko Eating Bananas
🔗  Link: [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, Binary Search<br>

=======================================================================================<br>
Koko loves to eat bananas. There are `n` piles of bananas, the ith pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.<br>

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.<br>

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.<br>

Return the minimum integer `k` such that she can eat all the bananas within `h` hours.



Example 1:<br>
Input: piles = [3,6,7,11], h = 8<br>
Output: 4<br>

Example 2:<br>
Input: piles = [30,11,23,4,20], h = 5<br>
Output: 30<br>

Example 3:<br>
Input: piles = [30,11,23,4,20], h = 6<br>
Output: 23<br>

Constraints:<br>
- 1 <= piles.length <= 10^4
- piles.length <= h <= 10^9
- 1 <= piles[i] <= 10^9

=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input matrix be empty? 
    - We don’t need to consider empty inputs
2. Any requirement on time/space complexity? 
    - You must write a solution in O(n⋅logm) time complexity and O(1) space complexity
3. Can the row size be different from the column size?
    - Yes, the row size can be different from the column size


### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. Binary Search <br>
Binary search is a method for locating an element in a sorted list efficiently. Searching for an element can be done naively in O(N) time, but binary search speeds it up to O(log N). Use binary search to locate the boundary that separates workable speeds and unworkable speeds, to get the minimum workable speed


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

- General Idea: If Koko can eat all the piles with a speed of `n`, she can also finish the task with the speed of `n+1`; if Koko can't finish with a speed of `n`, then she can't finish with the speed of `n−1`either
1) Initialization:
Set `left` to 1 (minimum possible eating speed), `right` to the maximum number of bananas in a pile, and `ans` to right (initialize the answer to the maximum possible speed).

2) Binary Search Loop:
While `left` is less than or equal to `right`, calculate the middle value and iterate through each pile of bananas to calculate hours to eat the bananas in the pile
- If `hours` > `h`, update `left = k + 1` (search for higher speed).
- If `hours` <= `h`, update `ans` to `min(ans, k)` and `right = k - 1` (search for lower speed).
3) Return Result:
Return the final answer `ans`, representing the minimum eating speed required.


### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Let n be the length of the input array piles and m be the maximum number of bananas in a single pile from piles.

- Time Complexity: O(n⋅logm)
- Space Complexity: O(1)
