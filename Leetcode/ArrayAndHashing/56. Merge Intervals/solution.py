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
        # Sort the intervals based on the start time
        intervals.sort(key=lambda x: x[0])

        merged = []  # Initialize a list to store the merged intervals
        for interval in intervals:  # Iterate through each interval
            # If the merged list is empty or the last interval in merged does not overlap with the current one,
            # append the current interval to merged
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # If the current interval overlaps with the last interval in merged,
                # update the end time of the last interval in merged to be the max of the current interval's end time and the last interval's end time
                merged[-1][1] = max(interval[1], merged[-1][1])

        return merged  # Return the list of merged intervals
