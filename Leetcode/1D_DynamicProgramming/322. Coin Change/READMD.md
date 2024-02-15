## 322. Coin Change
🔗  Link: [Coin Change](https://leetcode.com/problems/coin-change/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, DP<br>

=======================================================================================<br>
You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.<br>

Return the *fewest* number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.<br>

You may assume that you have an infinite number of each kind of coin.<br>

Example 1:<br>
Input: coins = [1,2,5], amount = 11<br>
Output: 3<br>
Explanation: 11 = 5 + 5 + 1<br>

Example 2:<br>
Input: coins = [2], amount = 3<br>
Output: -1<br>

Example 3:<br>
Input: coins = [1], amount = 0<br>
Output: 0<br>

Constraints:<br>
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4

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
        - Assume, coins = [1, 6, 7, 9, 11] , amount = 13. Going via the greedy way, we will pick the coin with the highest denomination first = 11. And then pick two 1s. Which makes it 13 = 11 + 1 + 1. And return answer as 3. But clearly, our answer is 13 = 6 + 7 which makes minimum number of coins as 2. 
    
    - **DP builds up the solution by considering smaller subproblems**. It explores all combinations, ensuring that the global optimal solution is found, which is especially important when certain combinations of smaller denominations might yield a better solution than using a larger denomination


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: by solving smaller sub-problems and using their results to solve larger ones, find the minimum number of coins needed to make up a given amount, where you have an unlimited supply of each coin in the given denominations (Bottom-Up Approach)

1) Coin Filtering: 
Filters out coins from the given list that are larger than the target amount, as they are not useful for making change.

2) Dynamic Programming Array Initialization: 
Creates a dynamic programming array `dp` *with a size one greater than the target amount*. It's initialized with some placeholder value (`amount + 1`) to represent the minimum number of coins needed, with the exception of `dp[0]` being set to `0`.(meaning to get to the value `0` we need `0` coin)

3) Calculating Minimum Coins for Each Amount: 
Iterates through each possible amount up to the target, using each coin to update `dp`. It calculates the minimum number of coins needed to make each amount by considering the current coin and the best previous result.

4) Solution Determination: Checks if the target amount can be achieved with the available coins. If `dp[amount]` is not the default value we set, it returns the minimum number of coins required; otherwise, it returns `-1`, indicating no solution with the given coins.



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

- Time Complexity: O(amount * n)
- Space Complexity: O(amount + 1) => O(amount)
