class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num

            if complement in hashmap:
                return [i, hashmap[complement]]
                
            hashmap[num] = i 


# improve the code above by using enumerate:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            if num in hashmap:
                return [i, hashmap[num]]
                
            # Store the counterpart of the number we have seen and the current index
            hashmap[target-num] = i

                
