## 121. Best Time to Buy and Sell Stock
🔗  Link: [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: Array, Sliding Window<br>

=======================================================================================<br>
You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:<br>
Input: prices = [7,1,5,3,6,4]<br>
Output: 5<br>
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.<br>

Example 2:<br>
Input: prices = [7,6,4,3,1]<br>
Output: 0<br>
Explanation: In this case, no transactions are done and the max profit = 0.<br>

Constraints:<br>
1 <= prices.length <= 10^5<br>
0 <= prices[i] <= 10^4<br>
=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input array be empty?
    - No, there is at least 1 day in the array
2. Any requirement on time/space complexity?
    - O(n) time and O(1) space will do.
3. Is the array sorted?
    - No
4. Will there be negative numbers in the array?
    - No

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. Sliding Window<br>
Keep track of the minimum price encountered so far and update the maximum profit whenever a higher selling price is found.

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Record the minimum price found as we proceed through the array and keep checking for a higher profit

1) Initialize `min_price` to the first element in the array and `max_profit` to 0
2) Iterate through the prices:
    - For each price:
        - Update `min_price` by taking the minimum of the current min_price and the current price
        - Update `max_profit` by taking the maximum of the current max_profit and the difference between the current price and min_price
3) After the iteration, `max_profit` will contain the maximum profit achievable
4) Return max_profit as the final result


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
- Space Complexity: O(1)
