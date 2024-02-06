class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Filter out coins larger than the amount
        coins = [coin for coin in coins if coin <= amount]

        # Initialize dp array
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        # Compute minimum number of coins for each amount
        for target_amount in range(1, amount + 1):
            for coin in coins:
                if target_amount >= coin:
                    dp[target_amount] = min(dp[target_amount], 1 + dp[target_amount - coin])

        # Check if a solution exists
        return dp[amount] if dp[amount] != float('inf') else -1
