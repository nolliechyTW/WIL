class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Combine position and speed into pairs
        pairs = sorted(zip(position, speed), reverse=True)

        stack = []
        for p, s in pairs:
            time_to_destination = (target - p) / s
            
            # Check if the current car can join the previous fleet
            while stack and time_to_destination <= stack[-1]:
                stack.pop()
                
            stack.append(time_to_destination)

        return len(stack)
