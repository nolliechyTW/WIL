class Solution:
    def trap(self, height: List[int]) -> int:
        """ O(n) in Time, O(1) in Space"""
        if not height:
            return 0

        n = len(height)
        
        # Find the index of the tallest bar
        peak_index = 0
        for i in range(1, n):
            if height[i] > height[peak_index]:
                peak_index = i

        # Accumulator for trapped water
        rainfall = 0

        # Process the left side of the peak
        left_max = 0
        for i in range(peak_index):
            left_max = max(left_max, height[i])
            rainfall += max(0, left_max - height[i])

        # Process the right side of the peak
        right_max = 0
        for i in range(n - 1, peak_index, -1):
            right_max = max(right_max, height[i])
            rainfall += max(0, right_max - height[i])

        return rainfall
