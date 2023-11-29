class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Combine position and speed into pairs and sort by position
        pairs = sorted(zip(position, speed), key=lambda x: x[0]) # from smallest to largest position

        # Stack to store the time it takes for each car to reach the destination
        stack = []

        # Iterate through the sorted pairs
        for p, s in pairs:
            # Calculate the time it takes for the current car to reach the destination
            time_to_destination = (target - p) / s

            # Check if the current car can join the previous fleet
            while stack and time_to_destination >= stack[-1]:
                stack.pop()

            # Add the current car's time to the stack
            stack.append(time_to_destination)

        # The length of the stack represents the number of car fleets
        return len(stack)