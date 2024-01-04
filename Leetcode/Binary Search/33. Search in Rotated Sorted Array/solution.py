class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize the pointers for the beginning and end of the array
        left, right = 0, len(nums) - 1

        # Continue searching while the left pointer is not greater than the right pointer
        while left <= right:
            # Calculate the middle index. This way of calculation avoids overflow
            mid = left + (right - left) // 2

            # Case 1: The middle element is the target
            # Check if the middle element is the target
            if nums[mid] == target:
                return mid

            # Case 2: The left half of the array is sorted
            # Check if the left half of the array is sorted
            if nums[left] <= nums[mid]:
                # Determine if the target is in the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Narrow the search to the left half
                else:
                    left = mid + 1  # Narrow the search to the right half
            # Case 3: The right half of the array is sorted
            else:
                # The right half must be sorted since the left half is not
                # Determine if the target is in the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # Narrow the search to the right half
                else:
                    right = mid - 1  # Narrow the search to the left half

        # Return -1 if the target is not found in the array
        return -1
