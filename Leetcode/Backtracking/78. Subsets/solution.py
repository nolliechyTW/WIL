class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            # Append a copy of path to results
            res.append(path[:])
            for i in range(start, len(nums)):
                # Add nums[i] into the current combination
                path.append(nums[i])
                # Move on to the next element
                backtrack(i + 1, path)
                # Backtrack
                path.pop()

        res = []
        backtrack(0, [])
        return res        
