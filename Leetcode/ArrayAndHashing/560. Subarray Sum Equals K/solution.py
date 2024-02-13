class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0 
        prefix_sum = 0  # keep the cumulative sum of elements as we iterate through 'nums'
        prefix_sum_count = {0: 1}  # A dictionary to store the frequency of prefix sums. Initialized with 0:1 because a prefix sum of 0 is considered once before starting.
        
        # Loop through each number in the given list 'nums'.
        for num in nums:
            prefix_sum += num  # Update the prefix sum with the current number.
            
            # Check if the current prefix sum minus 'k' exists in our prefix_sum_count dictionary.
            # This means there is a subarray ending at the current element which sums up to 'k'.
            if (prefix_sum - k) in prefix_sum_count:
                result += prefix_sum_count[prefix_sum - k]  # Add the frequency of (prefix_sum - k) to result.
            
            # Update the prefix_sum_count dictionary.
            if prefix_sum in prefix_sum_count:
                prefix_sum_count[prefix_sum] += 1  # If prefix_sum is already in the dictionary, increment its frequency.
            else:
                prefix_sum_count[prefix_sum] = 1  # Otherwise, add prefix_sum to the dictionary with frequency 1.

        # Return the total count of subarrays that sum up to 'k'.
        return result




## brute force - O(n^2) ; TLE
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        nums = 1, 2, 3, 2, 1
        current_sum = 1, 3, 6, 8, 9
        """
        count = 0
        n = len(nums)
        for start in range(n):
            current_sum = 0
            for end in range(start, n):
                current_sum += nums[end]
                if current_sum == k:
                    count += 1
        return count
