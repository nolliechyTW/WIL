



##############################################################################################################
# brute force - TLE
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0 
        right = k
        ans = []

        while right < len(nums)+1:
            maxNum = float('-inf')

            for i in range(left, right):
                maxNum = max(maxNum, nums[i])
            ans.append(maxNum)
            left += 1
            right += 1

        return ans

# improved brute force - TLE
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0 
        right = k
        ans = []

        while right <= len(nums):
            maxNum = max(nums[left:right])
            ans.append(maxNum)
            left += 1
            right += 1

        return ans