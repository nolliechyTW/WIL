## 146. LRU Cache
🔗  Link: [LRU Cache](https://leetcode.com/problems/lru-cache/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Linked List, Hashmap<br>

=======================================================================================<br>
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the `LRUCache` class:

- `LRUCache(int capacity)` Initialize the LRU cache with **positive** size `capacity`

- `int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`

- `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, evict the least recently used key.


Example 1:<br>
Input: <br>
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]<br>
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]<br>
Output:<br>
[null, null, null, 1, null, -1, null, -1, 3, 4]<br>

Explanation:<br>
LRUCache lRUCache = new LRUCache(2);<br>
lRUCache.put(1, 1); // cache is {1=1}<br>
lRUCache.put(2, 2); // cache is {1=1, 2=2}<br>
lRUCache.get(1);    // return 1<br>
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}<br>
lRUCache.get(2);    // returns -1 (not found)<br>
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}<br>
lRUCache.get(1);    // return -1 (not found)<br>
lRUCache.get(3);    // return 3<br>
lRUCache.get(4);    // return 4<br>


Constraints:<br>
- 1 <= capacity <= 3000
- 0 <= key <= 10^4
- 0 <= value <= 10^5
- At most 2 * 10^5 calls will be made to `get` and `put`

=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. What is an LRU?
    - A Least Recently Used (LRU) Cache organizes items in order of use, allowing you to quickly identify which item hasn't been used for the longest amount of time. An LRU cache is built by combining two data structures: a doubly linked list and a hash map
2. Any requirement on time/space complexity?
    - The functions `get` and `put` must each run in O(1) average time complexity.
3. Does the linked list have a cycle?
    - No


### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Linked List 
The doubly linked list maintains the order of elements based on their usage, allowing us to efficiently add, remove, and move elements to represent their usage.

2. Hashmap
The hash map provides O(1) average time complexity for lookups.
 
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: The hash table allows for fast access to cache items, while the doubly linked list maintains the items in order of their usage, with the most recently used items at the front. When a new item is added or an existing item is accessed, it is moved to the front of the list. If the cache exceeds its capacity, the least recently used item, found at the end of the list, is removed.

1) Get Operation
    - When `get(key)` is called:
        - Check if the key is in the hash table
            - If it's not there, return -1
            - If it is there, retrieve the node from the hash table
        - Move this node to the front of the doubly linked list to mark it as recently used
        - Return the value of the node

2) Put Operation
    - When `put(key, value) `is called:
        - First, check if the key is already in the cache
            - If it is, update the value of the node and move this node to the front of the list
            - If it's not in the cache:
                - Create a new node with the key and value
                - Add this node to the front of the list
                - Add the key and node reference to the hash table
                - If the cache is now over capacity:
                    - Remove the node from the tail of the list
                    - Remove the corresponding entry from the hash table

Visualization:
- Before Any Operation: Head <-> Tail
- After Some put Operations: Head <-> Node1 <-> Node2 <-> ... <-> NodeN <-> Tail
- After a get Operation on Node2: Head <-> Node2 <-> Node1 <-> ... <-> NodeN <-> Tail
- After Adding a New Node When at Full Capacity: Head <-> NewNode <-> Node1 <-> ... <-> Node(N-1) <-> Tail (NodeN is removed)

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N is the capacity of the cache

- Time Complexity: O(1) both for put and get
- Space Complexity: O(N) since the space is used only for a hashmap and double linked list with at most capacity + 1 elements