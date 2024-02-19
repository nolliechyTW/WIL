class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        if n == 1:  # If there's only one employee, no time is needed to inform.
            return 0

        # Initialize the total time taken to 0.
        time = 0
        
        # Build a mapping of managers to their direct reports.
        employees = defaultdict(list)
        for i, m in enumerate(manager):
            if m != -1:
                employees[m].append(i)  # Add employee to their direct manager's list

        # Use a deque to perform BFS, starting with the head manager.
        queue = deque([(headID, informTime[headID])])  # Store tuples of (employee ID, total time to inform this employee)

        while queue:
            curr, curr_time = queue.popleft()  # Get the current employee and their inform time.
            time = max(time, curr_time)  # Update the max time to ensure all employees are informed.

            # Add direct reports of the current employee to the queue.
            for subordinate in employees[curr]:
                queue.append((subordinate, curr_time + informTime[subordinate]))

        return time