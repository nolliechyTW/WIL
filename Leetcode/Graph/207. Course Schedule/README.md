## 207. Course Schedule
🔗  Link: [Course Schedule](https://leetcode.com/problems/course-schedule/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Topological Sort, DFS, BFS<br>

=======================================================================================<br>
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`.<br>

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`

Return `true` if you can finish all courses. Otherwise, return `false`.<br>


Example 1:<br>
Input: numCourses = 2, prerequisites = [[1,0]]<br>
Output: true<br>
Explanation: There are a total of 2 courses to take. <br>
To take course 1 you should have finished course 0. So it is possible.<br>

Example 2:<br>
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]<br>
Output: false<br>
Explanation: There are a total of 2 courses to take. <br>
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.<br>


Constraints:<br>
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- All the pairs prerequisites[i] are unique.

=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the prerequisites be empty?
    - Yes
2. Any requirement on time/space complexity?
    - O(V + E) in time and space complexity
3. Can a course have multiple prerequisites? For example, if prerequisites = [[0, 1], [0, 2]], does this mean to take course 0, one must complete both courses 1 and 2 first?
    - The ordering must respect the prerequisites but can vary otherwise
4. How should the algorithm handle circular dependencies? For example, prerequisites = [[0, 1], [1, 0]]?
    - `false`, as it is impossible to complete the courses due to a circular dependency

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Directed Acyclic Graph (DAG)
The problem essentially describes a Directed Acyclic Graph (DAG), where each course is a node, and a directed edge from course `bi` to course `ai` (as indicated by `[ai, bi]` in prerequisites) signifies that `bi` is a prerequisite of `ai`. **Topological sorting** is used specifically for DAGs to find a linear ordering of its vertices.

2. Topological Sorting
The problem asks for an ordering of courses such that for every directed edge from course bi to course ai, bi comes before ai. This is precisely what topological sorting achieves - it orders vertices of a DAG in such a way that every directed edge points from an earlier vertex to a later vertex in the ordering.

3. BFS
The BFS variant of topological sort (also known as `Kahn's algorithm`) is particularly useful because it can simultaneously provide the topological order and check for cycles. It involves iteratively removing nodes with no incoming edges (i.e., courses with no prerequisites) and reducing the incoming edge count for adjacent nodes. If at any point there are no nodes with zero incoming edges, it means a cycle exists.


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: The algorithm first constructs a directed graph from the course prerequisites. It then uses a queue to process each course, determining whether all courses can be completed. It returns `false` if it's not possible to complete all courses

1) Initialize Data Structures:
    - `indegree`: An **array** to keep track of the number of prerequisites (inbound edges) for each course
    - `graph`: A **dictionary** to represent the adjacency list of the graph, where keys are courses and values are lists of courses that depend on them

2) Build the Graph and Indegree Array:
    - Loop through each pair in `prerequisites`. For each pair `[course, preq]`, add `course` to the adjacency list of `preq` in the graph. This represents that course has `prereq` as a prerequisite.
    - Increment the indegree of `course` by 1, as it has an additional prerequisite.

3) Initialize the Queue:
    - Create a queue to process all courses that have no prerequisites (indegree of 0). These courses can be taken immediately.
    - Use a list comprehension to add all courses with an indegree of 0 to the queue.

4) Process the Queue:
    - While the `queue` is not empty, dequeue a course.
    - For each course dependent on the dequeued course (accessible from the graph), decrement its indegree by 1, indicating that one of its prerequisites has been completed.
    - If the indegree of any dependent course becomes 0, enqueue it, as it can now be taken.

5) Check for Completion:
    - After processing the queue, check if all `indegrees` are zero by iterating over the indegree array.
    - If all courses have an indegree of 0, return `True`, indicating all courses can be completed.
    - If not, return `False`, indicating that not all courses can be completed due to a cycle or unmet prerequisites.

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N is the number of courses, P is the number of prerequisites.

- Time Complexity: O(N + P)
- Space Complexity: O(N + P)