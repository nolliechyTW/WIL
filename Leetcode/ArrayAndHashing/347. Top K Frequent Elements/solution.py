# use bucket sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq = [[] for i in range(len(nums))]
        
        for i in nums:
            count[i] = count.get(i, 0) + 1
            
        for key, value in count.items():
            freq[value-1].append(key)
            
        ans = []
        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans

# use Hash Map with Frequency Count and Sorting
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        
        # Count the frequency of each element
        for num in nums:
            if num in frequency_map:
                frequency_map[num] += 1
            else:
                frequency_map[num] = 1

        # Sort elements based on their frequencies and values (descending order)
        sorted_elements = sorted(nums, key=lambda x: (-frequency_map[x], x))

        # Remove duplicates while maintaining order
        sorted_elements = list(dict.fromkeys(sorted_elements))

        # Return the top k elements from the sorted list
        return sorted_elements[:k]

# use Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # assume nums = [3, 3, 3, 3, 2, 2, 1]
        counter = Counter(nums) # Counter({3: 4, 2: 2, 1: 1})
        most_common = counter.most_common(k) # [(3, 4), (2, 2)]
        result = []
        for item in most_common:
            result.append(item[0]) 
        return result # [3, 2]

# use list comprehension and Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            return [item[0] for item in Counter(nums).most_common(k)]

