class TimeMap:
    def __init__(self):
        self.store = {}  # key: list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        """O(1) in Time"""
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        """O(log n) in Time"""
        values = self.store.get(key, [])  # dictionary get method
        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] == timestamp:
                # Found an exact match for the timestamp
                return values[mid][0]
            elif values[mid][1] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        # If no exact match is found, return the value corresponding to the
        # largest timestamp smaller than the target timestamp (values[right][0])
        # or an empty string if there is no such value.
        return values[right][0] if right >= 0 else ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)