class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # Precompute the prefix sums of candles and the nearest candle positions to the left and right
        n = len(s)
        prefix_sum = [0] * n
        left_nearest_candle = [-1] * n
        right_nearest_candle = [n] * n

        candle_count = 0
        for i in range(n):
            if s[i] == '|':
                candle_count += 1
                left_nearest_candle[i] = i
            else:
                if i > 0:
                    left_nearest_candle[i] = left_nearest_candle[i - 1]
            prefix_sum[i] = candle_count

        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                right_nearest_candle[i] = i
            else:
                if i < n - 1:
                    right_nearest_candle[i] = right_nearest_candle[i + 1]

        # Process each query
        answer = []
        for left, right in queries:
            # Find the nearest candles to the left and right within the range
            left_candle = right_nearest_candle[left]
            right_candle = left_nearest_candle[right]

            # Check if there is at least one candle to the left and right
            if left_candle < right_candle:
                plates_count = (right_candle - left_candle + 1) - (prefix_sum[right_candle] - prefix_sum[left_candle] + 1)
                answer.append(plates_count)
            else:
                answer.append(0)

        return answer