class Solution:
    def minSwaps(self, data: List[int]) -> int:
        total_ones = sum(data)
        current_ones_count = max_ones_in_window = 0
        left = 0

        for right in range(len(data)):
            # Add the new element to the current count of 1's
            current_ones_count += data[right]

            # If the window is larger than total_ones, adjust the window from the left
            if right - left + 1 > total_ones:
                current_ones_count -= data[left]
                left += 1

            # Update the maximum number of 1's found in any window so far
            max_ones_in_window = max(max_ones_in_window, current_ones_count)

        return total_ones - max_ones_in_window
