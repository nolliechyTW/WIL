# beat 72% in time - [left, right]
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1

        if (left == right) and (nums[left] != target):
            return -1

        while left <= right:
            mid = (left + right) // 2  
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1 

# what if we want to find [left, right)?
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums)

        if left >= right:
            return -1

        while left < right:
            mid = (left + right) // 2  
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        
        return -1 