## 380. Insert Delete GetRandom O(1)
🔗  Link: [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, HashTable, Randomized<br>

=======================================================================================<br>
Implement the RandomizedSet class:

- `RandomizedSet()` Initializes the `RandomizedSet` object.
- `bool insert(int val)` Inserts an item `val` into the set if not present. Returns `true` if the item was not present, `false` otherwise.
- `bool remove(int val)` Removes an item `val` from the set if present. Returns `true` if the item was present, `false` otherwise.
- `int getRandom()` Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average `O(1)` time complexity.<br>

Example 1:<br>
Input: ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]<br>
[[], [1], [2], [2], [], [1], [2], []]<br>
Output: [null, true, false, true, 2, true, false, 2]<br>
Explanation: RandomizedSet randomizedSet = new RandomizedSet();<br>
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.<br>
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.<br>
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].<br>
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.<br>
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].<br>
randomizedSet.insert(2); // 2 was already in the set, so return false.<br>
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.<br>


Constraints:<br>
- -2^31 <= val <= 2^31 - 1
- At most 2 * `10^5` calls will be made to `insert`, `remove`, and `getRandom`.
- There will be at least `one` element in the data structure when `getRandom` is called.

=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Is it acceptable to use the standard library's random number generator for the `getRandom` method?
    - Yes
2. Any requirement on time/space complexity?
    - You must implement the functions of the class such that each function works in average `O(1)` time complexity
3. When an element is removed, should the remaining elements retain their order, or is it acceptable to swap elements to ensure O(1) deletion?
    - It is ok to swap


### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1) List:
The list stores the values and allows for O(1) append operations and O(1) access to a random element by index.

2) Map: 
The map (dictionary) keeps track of the indices of the elements in the list, allowing for O(1) lookup to check if a value is in the set and O(1) removal by index.


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: 

1) Initial Setup
- `myMap`: A dictionary (or **map**) that maps each value inserted into the set to its index in myList. This allows for O(1) lookup time to check if a value exists in the set and to find its index if it does
- `myList`: A **list** that stores all the values in the set. This structure enables O(1) time complexity when adding a new value (by appending to the end) and when retrieving a random value (by using random selection)

2) Insertion (insert method)
- When inserting a new value `val`, first check if it exists in myMap. If it does, return `False` since duplicates are not allowed
- If `val` is not in myMap, add it to myMap *with its index in myList being the length of myList before val is appended*. This ensures val is correctly mapped to its position
- Append val to myList and return `True`

3) Deletion (remove method)
- To remove a value `val`, first check if it exists in myMap
- If it doesn't, return `False`
- If `val` exists, find its index using myMap
- Swap `val` with the **last element** in myList to ensure that removal can be done in 
O(1) time by simply popping the last element
- Update myMap to reflect the new index of the element that was swapped with val
- *Pop the last element from myList*, effectively *removing `val`*
- Delete `val` from myMap
- Return True

4) Retrieving a Random Element (getRandom method)
Use `random.choice(self.myList)` to return a random element from myList. This operation is O(1) because it randomly indexes into the list.

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume there are `N` operations. 

- Time Complexity: O(1)
- Space Complexity: O(N)
