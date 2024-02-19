import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Use a min heap with a maximum size of k
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        # The root of the heap is the kth largest element
        return heap[0]
    
    
# better solution - counting sort 