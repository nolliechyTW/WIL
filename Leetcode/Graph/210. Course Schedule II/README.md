## 210. Course Schedule II
🔗  Link: [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Topological Sort, DFS, BFS<br>

=======================================================================================<br>
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`.<br>

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.<br>

Example 1:<br>
Input: numCourses = 2, prerequisites = [[1,0]]<br>
Output: [0,1]<br>
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].<br>

Example 2:<br>
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]<br>
Output: [0,2,1,3]<br>
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.<br>
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].<br>

Example 3:<br>
Input: numCourses = 1, prerequisites = []<br>
Output: [0]<br>

Constraints:<br>
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= numCourses * (numCourses - 1)
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- ai != bi
- All the pairs [ai, bi] are distinct.

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
    - `[]`, as it is impossible to complete the courses due to a circular dependency.

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

General Idea: first constructs a directed graph from the course prerequisites, then uses a queue to determine a valid order of course completion, **returning an empty list if such an order is not possible**.

1) Initialize Data Structures:
    - `indegree`: An **array** to keep track of the number of prerequisites (inbound edges) for each course
    - `graph`: A **dictionary** to represent the adjacency list of the graph, where keys are courses and values are lists of courses that depend on them

2) Build the Graph and Indegree Array:
    - Loop through each pair in `prerequisites`. For each pair `[course, preq]`, add `course` to the adjacency list of `preq` in the graph. This represents that to take `course`, one must first complete `preq`.
    - Increment the indegree of `course` by 1, as it has an additional prerequisite.

3) Initialize the Queue:
    - Create a queue to process all courses that have no prerequisites (indegree of 0). These courses can be taken immediately.
    - Iterate through all courses, and enqueue those with an indegree of 0.

4) Process the Queue:
    - While the `queue` is not empty, perform the following:
        - Dequeue an element, say `course`. Add `course` to the result list `res`, representing that this course can be taken next.
        - Iterate over all the courses dependent on `course` (accessible from the `graph`). For each such course, decrement its indegree by 1, indicating that one of its prerequisites has been met.
        - If the indegree of any dependent course becomes `0`, enqueue it, as it is now ready to be taken.

5) Check for Completion:
    - After processing the queue, if the length of `res` is equal to `numCourses`, it means all courses can be completed in the order stored in `res`. Return `res`.
    - If not, it indicates that not all courses can be completed due to a cycle (or unmet prerequisites), and therefore, return an empty list.

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

V represents the number of vertices(the number of courses) and E represents the number of edges(the number of prerequisites).

- Time Complexity: O(V + E); as both the courses and their relationships (prerequisites) are processed once
- Space Complexity: O(V + E); the graph uses O(V+E) space, as it stores a list of dependents for each course. In the worst case, it might store every prerequisite relationship