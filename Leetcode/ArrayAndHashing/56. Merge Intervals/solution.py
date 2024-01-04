class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        
        for low, high in sorted(intervals):
            if not result:
                result.append([low, high])
            prevHigh = result[-1][1]
            if prevHigh >= low:
                result[-1][1] = max(prevHigh, high)
            else:
                result.append([low, high])

        return result
    

# improved solution
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(interval[1], merged[-1][1])

        return merged