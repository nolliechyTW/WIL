# brute force
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []

        for factor in range(1, n + 1):
            if n % factor == 0:
                factors.append(factor)

        if len(factors) < k:
            return -1
        return factors[k - 1]

# optimized
# Time Complexity: O(N**(1/2))
# Space Complexity: O(min(k, N**(1/2))) to store the list of divisors
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        divisors, sqrt_n = [], int(n**0.5)

        # If k drops down to zero during the iterations - the kth divisor is here. 
        for x in range(1, sqrt_n + 1):
            if n % x == 0:
                divisors.append(x)
                k -= 1 # k is decremented each time a factor is found. 
                if k == 0: # If k reaches 0, it means we've found the kth factor 
                    return x
        
        
        if (sqrt_n * sqrt_n == n): # If n is a perfect square, we have to skip the duplicate in the divisor list
            k += 1
        
        # Otherwise, the kth divisor is the paired one and could be found as  n // divisors[n_div - k] 
        n_div = len(divisors)
        return n // divisors[n_div - k] if k <= n_div else -1
