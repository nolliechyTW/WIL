class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        indegree = [0] * numCourses
        graph = defaultdict(list)

        for course, preq in prerequisites:
            graph[preq].append(course)
            indegree[course] += 1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        res = []
        while queue:
            course = queue.popleft()
            res.append(course)
            for dependency in graph[course]:
                indegree[dependency] -= 1
                if indegree[dependency] == 0:
                    queue.append(dependency)
        
        return res if len(res) == numCourses else [] # key 


