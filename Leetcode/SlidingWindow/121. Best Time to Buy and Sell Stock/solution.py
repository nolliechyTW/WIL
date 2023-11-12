class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]

        for price in prices:
            # Record the minimum price found as we proceed through the array
            minPrice = min(price, minPrice)
            # Check for a higher profit
            maxProfit = max(maxProfit, price - minPrice)
        
        return maxProfit

