## binary search
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        # Ensure nums1 is the shorter array
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        total_len = m + n
        mid_point = (m + n + 1) // 2

        low, high = 0, n

        while low <= high:
            mid1 = (low + high) // 2
            mid2 = mid_point - mid1

            l1 = float('-inf') if mid1 == 0 else nums1[mid1 - 1]
            l2 = float('-inf') if mid2 == 0 else nums2[mid2 - 1]
            r1 = float('inf') if mid1 == m else nums1[mid1]
            r2 = float('inf') if mid2 == n else nums2[mid2]

            # Check for valid partition
            if l1 <= r2 and l2 <= r1:
                if total_len % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1

        return 0.0


## brute force
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Merge the arrays into a single sorted array.
        merged = nums1 + nums2
        merged.sort()

        # Calculate the total number of elements in the merged array.
        total = len(merged)

        if total % 2 == 1:
            # If the total number of elements is odd, return the middle element as the median.
            return float(merged[total // 2])
        else:
            # If the total number of elements is even, calculate the average of the two middle elements as the median.
            middle1 = merged[total // 2 - 1]
            middle2 = merged[total // 2]
            return (float(middle1) + float(middle2)) / 2.0