from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create a graph and an array to store the indegree of each node
        graph = defaultdict(list)
        indegree = [0] * numCourses

        # Build the graph and update the indegree
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        # Initialize a queue and add all courses with indegree 0
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        # Process the queue
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Check if all indegrees are zero
        return all(indegree[i] == 0 for i in range(numCourses))
