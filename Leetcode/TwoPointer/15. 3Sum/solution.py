class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # Sort the input array in ascending order
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: # Avoid duplicates for the first number in the triplet
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    # Avoid duplicates for the second number in the triplet
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Avoid duplicates for the third number in the triplet
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result        