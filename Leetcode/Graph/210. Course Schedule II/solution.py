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
            ans = queue.popleft()
            res.append(ans)
            for dependency in graph[ans]:
                indegree[dependency] -= 1
                if indegree[dependency] == 0:
                    queue.append(dependency)
        
        if len(res) == numCourses:
            return res
        else:
            return []


