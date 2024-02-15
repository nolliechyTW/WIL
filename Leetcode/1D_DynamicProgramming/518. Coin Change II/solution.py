class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Initialize a list to hold the number of combinations for each amount up to the target amount.
        # The size is amount + 1 because we include 0 as a possible amount to make change for.
        dp = [0] * (amount + 1)
        
        # Base case: There is exactly 1 way to make change for 0 amount, which is not using any coins.
        dp[0] = 1  

        # Iterate over each coin in the list of coins.
        for coin in coins:
            # For each coin, update the combinations for making change for amounts from the coin's value to the target amount.
            for current in range(coin, amount + 1):
                # For the current amount (current), add the number of ways to make (current - coin).
                # This is because each way to make (current - coin) can form a new combination with this coin
                # to make current. It effectively "extends" each of those combinations by this coin.
                dp[current] += dp[current - coin]

        # After processing all coins, dp[amount] will contain the total number of ways to make change for the target amount.
        return dp[amount]
