class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num

            if complement in hashmap:
                return [i, hashmap[complement]]
                
            # Store the counterpart of the number we have seen and current index
            hashmap[num] = i 


# improve the code above by using enumerate:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            if num in hashmap:
                return [i, hashmap[num]]
            hashmap[target-num] = i

                