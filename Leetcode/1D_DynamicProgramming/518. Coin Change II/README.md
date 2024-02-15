## 518. Coin Change II
🔗  Link: [Coin Change II](https://leetcode.com/problems/coin-change-ii/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, DP<br>

=======================================================================================<br>
You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.<br>

Return the *number* of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return *0*.<br>

You may assume that you have an infinite number of each kind of coin.<br>

The answer is guaranteed to fit into a signed 32-bit integer.
<br>


Example 1:<br>
Input: amount = 5, coins = [1,2,5] <br>
Output: 4<br>
Explanation: there are four ways to make up the amount:<br>
5=5<br>
5=2+2+1<br>
5=2+1+1+1<br>
5=1+1+1+1+1<br>

Example 2:<br>
Input: amount = 3, coins = [2]<br>
Output: 0<br>
Explanation: the amount of 3 cannot be made up just with coins of 2.<br>

Example 3:<br>
Input: amount = 10, coins = [10]<br>
Output: 1<br>


Constraints:<br>
- 1 <= coins.length <= 300<br>
- 1 <= coins[i] <= 5000<br>
- All the values of coins are unique.<br>
- 0 <= amount <= 5000<br>

=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Are the coin denominations always positive integers?
    - Yes
2. Any requirement on time/space complexity?
3. Does the order of denominations in the array matter? For instance, is [1, 2, 5] different from [5, 1, 2]?
    - No; What is important is the set of denominations available, not the order in which they are presented

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1)  Dymanic Programming <br>
    - Dealing with an optimization problem, we usually use either DP or greedy algorithm to solve it. The best way of doing this is by drawing an example and playing around with it. Here we go with DP
    - DP is a more robust solution because it explores all possible combinations of coins to find the minimum number of coins needed. This is crucial when the coin denominations don't follow a specific pattern or when larger denominations are not multiples of smaller ones

    - **DP builds up the solution by considering smaller subproblems**. It explores all combinations, ensuring that the global optimal solution is found, which is especially important when certain combinations of smaller denominations might yield a better solution than using a larger denomination

    - 

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: implement a dynamic programming solution to calculate the number of ways to make change for a given amount using a set of coins, by building up from smaller to larger amounts and reusing intermediate results to efficiently find the final answer; we iteratively update a table to keep track of all possible combinations for each amount, culminating in the total combinations for the target amount

1) Initialize a Table: 
- Create a table (array) to store the number of ways to make change for amounts from 0 up to the target amount. 
- Initialize this table such that there are zero ways to make change for any amount, except for the base case where the amount is 0. 
- For amount 0, set the number of ways to 1, because there is exactly one way to make change for amount 0, which is to use no coins at all.

2) Process Each Coin One by One: 
- Iterate through each coin available. For each coin, you're going to update the table to reflect the number of ways to make change for amounts that can include this coin.

3) Update the Table for Each Coin: 
- For the current coin, iterate through the amounts from the coin's value up to the target amount. 
- For each of these amounts, update the table to add the number of ways to make change for this amount by including the current coin. This is done by adding the number of ways to make change for the amount that is the current amount minus the value of the coin.

4) How the Update Works: 
When you're updating the table for a specific amount, you're effectively saying, **"For the current amount, I can increase the number of ways to make change by looking at how many ways I could make change for the amount that's the current amount minus this coin's value."** This process leverages the principle that if you can make change for a smaller amount, you can extend those ways to make change for a larger amount by adding the current coin.

5) Final Result: After iterating through all coins and updating the table for each coin across all relevant amounts, the value in the table corresponding to the target amount will be the total number of ways to make change for that amount using the available coins.


### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume there are `N` coin denominations.

- Time Complexity: O(amount * N)
- Space Complexity: O(amount + 1) => O(amount)
