# Using counting sort
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n, icecreams = len(costs), 0
        m = max(costs)

        costsFrequency = [0] * (m + 1)
        for cost in costs:
            costsFrequency[cost] += 1

        for cost in range(1, m + 1):
            if not costsFrequency[cost]:
                continue
            if coins < cost:
                break
            # costsFrequency[cost]: The total number of ice cream bars available at this cost
            # coins // cost: The maximum number of ice cream bars that can be afforded with the remaining coins
            count = min(costsFrequency[cost], coins // cost)
            coins -= cost * count
            icecreams += count
            
        return icecreams


# brute force
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # Filtering Costs <= Coins
        costs = [cost for cost in costs if cost <= coins]
        if len(costs) == 0 :
            return 0

        #  Not as efficient for this scenario as counting sort could be
        costs.sort()
        cnt = 0
        for cost in costs:
            if cost <= coins and coins > 0:
                cnt +=1
                coins -= cost

        return cnt