# O(log(m * n)) in Time, O(1) in Space 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        # Treat the matrix as a sorted 1D array and perform binary search.
        left = 0
        right = rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            mid_value = matrix[mid // cols][mid % cols] # key

            if mid_value == target:
                return True
            elif mid_value > target:
                right = mid - 1
            else:
                left = mid + 1

        return False


# m log n solution
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            left = 0
            right = cols - 1
            while left <= right:
                mid = (left + right) // 2
                if matrix[r][mid] == target:
                    return True
                elif matrix[r][mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        return False
