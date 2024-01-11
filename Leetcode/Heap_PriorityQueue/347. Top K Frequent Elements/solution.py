import heapq
from collections import Counter

def findKMostFrequent(nums, k):
    # Step 1: Count frequencies
    frequency_map = Counter(nums)

    # Step 2: Use heap to keep track of k most frequent elements
    min_heap = []
    for num, freq in frequency_map.items():
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # Step 3: Extract k most frequent elements
    most_frequent = [num for freq, num in min_heap]
    return most_frequent


## another solution using Bucket Sort for O(n) time complexity
from collections import Counter

def findKMostFrequent(nums, k):
    # Step 1: Count frequencies
    frequency_map = Counter(nums)

    # Step 2: Bucket Sort the frequencies
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in frequency_map.items():
        buckets[freq].append(num)

    # Step 3: Collect top k frequent elements
    most_frequent = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            most_frequent.append(num)
            if len(most_frequent) == k:
                return most_frequent

# Example Usage
nums = [1,1,1,2,2,3]
k = 2
print(findKMostFrequent(nums, k))  # Output: [1, 2] or [2, 1]
