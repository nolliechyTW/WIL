# Sliding Window approach : time complexity O(n) and space complexity O(1)

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Initialize the minimum length to a large value
        min_len = float('inf')
        left = 0  # The left pointer of the sliding window
        current_sum = 0  # The sum of the current subarray
        
        # Iterate through the array with the right pointer
        for right in range(len(nums)):
            # Add the current number to the current_sum
            current_sum += nums[right]
            
            # While the current_sum is equal to or exceeds the target,
            # update min_len and shrink the window from the left
            while current_sum >= target:
                # Update min_len to the smaller value between its current value and the window size
                min_len = min(min_len, right - left + 1)
                # Subtract the leftmost value from current_sum and move the left pointer to the right
                current_sum -= nums[left]
                left += 1
        
        # If min_len was updated, return its value; otherwise, return 0
        return min_len if min_len != float('inf') else 0

# Follow up: figure out a O(nlogn) solution
# Binary search approach : time complexity O(nlogn) and space complexity O(n)
    