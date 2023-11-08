class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # initialize two pointers
        left = 0 
        right = len(numbers) - 1 
        ans = []
        while left < right:
            if target == (numbers[left] + numbers[right]):
                ans.append(left+1) # add 1 to the index since the question is 1-indexed
                ans.append(right+1)
                return ans
            elif target < (numbers[left] + numbers[right]): # if the total exceeds target
                right -= 1
            else: # if the total is less than target
                left += 1
        
        

# follow up: improve time complexity to O(nlogn) using binary search       
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            complement = target - numbers[i] 
            left = i + 1 # We can start searching from the next element
            right = len(numbers) - 1 # Binary search will be performed on the remaining elements

            while left <= right: # find the complement using binary search
                mid = left + (right - left) // 2

                if numbers[mid] == complement:
                    return [i + 1, mid + 1]  # Found a pair

                elif numbers[mid] < complement:
                    left = mid + 1 

                else:
                    right = mid - 1 