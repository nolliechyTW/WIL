class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # create set
        distinctSet = set()

        # iterate through numbers
        for num in nums:
            # if number is already in set return True
            if num in distinctSet:
                return True
            # else store number in set
            else:
                distinctSet.add(num)
        # return false if we have reached the end of the list without duplicate
        return False
    