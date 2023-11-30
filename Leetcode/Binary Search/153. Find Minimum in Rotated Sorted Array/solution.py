class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # If nums[mid] is less than or equal to nums[right], 
                # it indicates that there is no rotation in the right portion of the midpoint. 
                # The minimum element should be in the left half or could be the midpoint itself. 
                # Therefore, update right = mid.
                right = mid
        
        return nums[right]