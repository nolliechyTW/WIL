## 1833. Maximum Ice Cream Bars
🔗  Link: [Maximum Ice Cream Bars](https://leetcode.com/problems/maximum-ice-cream-bars/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, Sorting, Greedy<br>

=======================================================================================<br>
It is a sweltering summer day, and a boy wants to buy some ice cream bars.

At the store, there are `n` ice cream bars. You are given an array costs of length `n`, where `costs[i]` is the price of the `ith` ice cream bar in coins. The boy initially has `coins` coins to spend, and he wants to buy as many ice cream bars as possible. 

Note: The boy can buy the ice cream bars in any order.

Return the maximum number of ice cream bars the boy can buy with `coins` coins.

You must solve the problem by counting sort.<br>

Example 1:<br>
Input: costs = [1,3,2,4,1], coins = 7<br>
Output: 4<br>
Explanation:<br>
The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.<br>

Example 2:<br>
Input: costs = [10,6,8,7,7,8], coins = 5<br>
Output: 0<br>
Explanation:<br>
The boy cannot afford any of the ice cream bars.<br>

Example 3:<br>
Input: costs = [1,6,3,1,2,5], coins = 20
Output: 6<br>
Explanation:<br>
The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.<br>

Constraints:<br>
- costs.length == n
- 1 <= n <= 10^5
- 1 <= costs[i] <= 10^5
- 1 <= coins <= 10^8
=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Is there a specific reason you want to solve this problem using counting sort instead of other sorting algorithms? 
    - Using counting sort, we can access the elements in sorted order in linear time
2. Any requirement on time/space complexity?
    - O(n) time complexity and O(1) space complexity
3. Are there any constraints on the prices of the ice cream bars, such as if they can only be whole numbers or if there's a maximum price for any ice cream bar?


### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. Counting Sort<br>
Counting sort is a sorting technique that is based on the keys between specific ranges. We store each element's frequency in an array and thus using this new array we can access all elements in sorted order.
As the input array's element's range is not very large, we can use counting sort here.


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: by using a frequency array to count the availability of ice cream bars at each cost level, the algorithm can quickly determine the best purchases to make within the budget constraints. Starting from the lowest cost ensures that the maximum number of ice cream bars is bought, as buying cheaper bars first allows for a larger quantity of purchases before funds are exhausted

1) Initialize Variables: <br>
Determine the number of ice cream bars (`n`) and set the initial count of purchased ice creams to 0. Find the maximum cost (`m`) among all ice cream bars to define the range of possible costs.

2) Create and Fill Frequency Array:<br>
- Initialize an array (costsFrequency) with a length of `m + 1` to account for all possible costs from 0 to m, setting all initial values to 0
- Iterate through each ice cream bar cost in the `costs` list, incrementing the corresponding index in costsFrequency to count the number of ice cream bars available at each cost

3) Iterate Through Possible Costs:<br>
- For each cost value starting from 1 up to m (inclusive), perform the following checks and operations:
    - Skip Costs with No Availability: If there are no ice cream bars available at a certain cost (indicated by a 0 in costsFrequency at the current cost), continue to the next cost.
    - Check for Sufficient Coins: If the current amount of coins is less than the cost being considered, exit the loop as no more purchases can be made.
    - Calculate Purchase: Determine the number of ice cream bars that can be bought at the current cost, **constrained by either the number of bars available at that cost or the number of bars that can be afforded with the remaining coins**.
    - Update Coins and Count: Subtract the total cost of the purchase from the remaining coins and add the number of bars bought to the total count of ice cream bars purchased.

4) Return Total Ice Creams Bought: <br>
After iterating through all possible costs or exiting early if coins are depleted, return the total count of ice cream bars purchased.


### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N is the length of the array `costs` and M is the maximum element in it.

- Time Complexity: O(N + M)
- Space Complexity: O(M)