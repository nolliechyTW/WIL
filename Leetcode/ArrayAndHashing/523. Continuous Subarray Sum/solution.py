class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Dictionary to store the first occurrence of a cumulative sum modulus k
        # Initialize with {0: -1} to handle the case where the subarray starts from the beginning
        sum_mod_k = {0: -1}
        curr_sum = 0  # Initialize current sum
        if k == 0:
            return True if len(nums) > 1 and sum(nums) == 0 else False
        
        for i, num in enumerate(nums):
            curr_sum += num  # Update the cumulative sum
            curr_sum %= k  # Take modulus to find the remainder of curr_sum / k
            
            # If curr_sum % k has been seen before, check if the subarray length is at least 2
            if curr_sum in sum_mod_k:
                if i - sum_mod_k[curr_sum] > 1:  # Ensure the subarray length is at least two
                    return True
            else:
                # Store the first occurrence of this sum mod k
                sum_mod_k[curr_sum] = i
        
        return False
