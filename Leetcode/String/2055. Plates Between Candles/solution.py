## prefix sum solution
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        prefix_sum = [0] * n
        candle_left = [-1] * n
        candle_right = [n] * n

        # Precompute prefix sum and nearest left candle
        prefix_sum[0] = 1 if s[0] == '*' else 0
        candle_left[0] = 0 if s[0] == '|' else -1
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + (1 if s[i] == '*' else 0)
            candle_left[i] = i if s[i] == '|' else candle_left[i - 1]

        # Precompute nearest right candle
        candle_right[n - 1] = n - 1 if s[n - 1] == '|' else n
        for i in range(n - 2, -1, -1):
            candle_right[i] = i if s[i] == '|' else candle_right[i + 1]

        # Process queries
        result = [0] * len(queries)
        for i in range(len(queries)):
            start = candle_right[queries[i][0]]
            end = candle_left[queries[i][1]]
            result[i] = 0 if start >= end else prefix_sum[end] - prefix_sum[start]

        return result


## binary search solution
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # Create a list of indices where candles are found
        candle_indices = [i for i, char in enumerate(s) if char == '|']
        
        def find_plates(left: int, right: int) -> int:
            # Use binary search to find the leftmost candle index greater than or equal to 'left'
            left_idx = bisect.bisect_left(candle_indices, left)
            # Use binary search to find the rightmost candle index less than or equal to 'right'
            right_idx = bisect.bisect_right(candle_indices, right) - 1
            
            # If there are not enough candles to form a valid segment, return 0
            if left_idx >= right_idx:
                return 0
            
            # Calculate the total plates between the two nearest candles
            return candle_indices[right_idx] - candle_indices[left_idx] - (right_idx - left_idx)
        
        # Process each query and calculate the number of plates between candles
        return [find_plates(left, right) for left, right in queries]


