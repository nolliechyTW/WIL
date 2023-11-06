class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Keep track of longestStreak starting at 0.
        longest_streak = 0
        # Create a hashset 
        num_set = set(nums)
        
        # Loop through the number set
        for num in num_set:
            # If current number has no previous number, then start counting from this number
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                # While the set contains currentNum + 1, increment currentNum and currentStreak
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                # After each while loop, check and set longestStreak
                longest_streak = max(longest_streak, current_streak)
        
        # Return longestStreak
        return longest_streak