# brute force - TLE
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0 

        for left in range(len(height) - 1):
            right = left + 1
            while right < len(height):
                area = (right - left) * min(height[left], height[right])
                ans = max(ans, area)
                right += 1
        return ans

# improved two pointer 
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            width = right - left
            maxArea = max(maxArea, min(height[left], height[right]) * width)
            if height[left] <= height[right]: # key
                left += 1
            else:
                right -= 1
                
        return maxArea