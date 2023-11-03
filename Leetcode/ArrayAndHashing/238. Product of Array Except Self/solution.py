# intuitive solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_products = [1] * n
        right_products = [1] * n

        left_product = 1
        for i in range(n):
            left_products[i] = left_product
            left_product *= nums[i] # for the next loop

        right_product = 1
        for i in range(n - 1, -1, -1):
            right_products[i] = right_product
            right_product *= nums[i]  # for the next loop

        result = [left_products[i] * right_products[i] for i in range(n)]
                
        return result

# follow up - O(1) space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = 1
        result = [1] * len(nums)

        for i in range(len(nums)):
            result[i] = left_product
            # Multiply product with the current number to develop left product
            left_product *= nums[i]
        
        # Create product from the right side of each num and multiply with the left product stored in output array.
        rightProduct = 1
        for j in range(len(nums) - 1,-1,-1):
            # Multiply right product with the left product stored in output array.
            result[j] *= rightProduct
            # Mutiply product with the current number to develop right product
            rightProduct *= nums[j]
        
        # Return the output array
        return result