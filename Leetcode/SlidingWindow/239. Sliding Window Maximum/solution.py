# using queue - O(n) 
# ref: https://www.youtube.com/watch?v=DfljaUwZsOk
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []  
        q = collections.deque()  # Deque to save indices in decreasing order based on their values in nums
        left = right = 0  # Initialize pointers for the sliding window

        while right < len(nums):
            # Save index in deque q in decreasing order based on their values in nums
            # Pop smaller values from the back of q to maintain decreasing order
            while q and nums[right] > nums[q[-1]]:
                q.pop()
            q.append(right)

            # Remove leftmost index from the window if it is no longer in the current window
            if left > q[0]:
                q.popleft()

            # If the window size is equal to or greater than k, append the maximum element in the window to the result list
            if (right + 1) >= k:
                res.append(nums[q[0]])
                left += 1  
            right += 1 

        return res 



##############################################################################################################
# brute force - TLE O(k(n-k))
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