## 36. Valid Sudoku

🔗 Link: [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, Hash<br>

=======================================================================================<br>
Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits `1-9` without repetition.
Each column must contain the digits `1-9` without repetition.
Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

Note:

- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

Example 1:<br>
Input: board = <br>
    [["5","3",".",".","7",".",".",".","."]<br>
    ,["6",".",".","1","9","5",".",".","."]<br>
    ,[".","9","8",".",".",".",".","6","."]<br>
    ,["8",".",".",".","6",".",".",".","3"]<br>
    ,["4",".",".","8",".","3",".",".","1"]<br>
    ,["7",".",".",".","2",".",".",".","6"]<br>
    ,[".","6",".",".",".",".","2","8","."]<br>
    ,[".",".",".","4","1","9",".",".","5"]<br>
    ,[".",".",".",".","8",".",".","7","9"]]<br>
Output: true<br>

Example 2:<br>
Input: board = <br>
    [["8","3",".",".","7",".",".",".","."]<br>
    ,["6",".",".","1","9","5",".",".","."]<br>
    ,[".","9","8",".",".",".",".","6","."]<br>
    ,["8",".",".",".","6",".",".",".","3"]<br>
    ,["4",".",".","8",".","3",".",".","1"]<br>
    ,["7",".",".",".","2",".",".",".","6"]<br>
    ,[".","6",".",".",".",".","2","8","."]<br>
    ,[".",".",".","4","1","9",".",".","5"]<br>
    ,[".",".",".",".","8",".",".","7","9"]]<br>
Output: false<br>
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.<br>

Constraints:<br>
board.length == 9 <br>
board[i].length == 9 <br>
board[i][j] is a digit 1-9 or '.' <br>
=======================================================================================<br>

### UMPIRE Method:

#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Any requirement on time/space complexity?

### Match

> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Storing the elements of the array in a Hashset<br>
   As we iterate through the array, we can store each number in a Set. If the number is already in the Hashset, then we can return True. Otherwise we reach the end of the array and return False.

### Plan

> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Create three Hashset to store number. If the number is already in the Hashset, then return True. Otherwise we reach the end of the array and return False.

1. Create Hashset using `defaultdict(set)` in python
2. Iterate through numbers()
   - If number is already in set return True
   - Else store number in set
3. Return False if we have reached the end of the list without duplicate

### Implement

> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review

> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

### Evaluate

> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Let N be the board length, which is 9 in this question. Since the value of N is fixed, the time and space complexity of this algorithm can be interpreted as O(1).
- Time Complexity: O(1)
- Space Complexity: O(1)


=======================================================================================<br>
### HashMap(dictionary) vs HashSet(set): Main Differences

- Purpose:
    - HashMap: HashMap is used to store key-value pairs. It allows you to associate a value with a unique key and retrieve the value based on the key. It provides fast access to values based on their keys.
    - HashSet: HashSet is used to store a collection of unique elements, with no associated values. It ensures that no duplicate elements are present in the set.

- Data Structure:
    - HashMap: HashMap is implemented as a hash table. It uses hashing to map keys to their corresponding values. Each key is unique, and the keys are used to look up the associated values.
    - HashSet: HashSet is also implemented as a hash table, but it stores only the keys (or elements) without associated values. It ensures uniqueness of elements in the set.

- Elements:
    - HashMap: It stores key-value pairs as entries, and the keys must be unique within the HashMap. Values can be duplicated.
    - HashSet: It stores individual elements, and each element must be unique within the set. There are no associated values.

- Access:
    - HashMap: You can access values in a HashMap by providing the corresponding key. It offers efficient key-based lookup operations.
    - HashSet: You can check for the presence of an element in a HashSet using the contains method. It doesn't have a direct key-based lookup, as it's designed for set membership tests.

- Iteration:
    - HashMap: You can iterate through the key-value pairs in a HashMap using methods like keySet, values, or entrySet.
    - HashSet: You can iterate through the elements in a HashSet using an enhanced for loop or an iterator.

- Performance:
    - HashMap: HashMap provides efficient key-based operations and is suitable for situations where you need to associate values with unique keys.
    - HashSet: HashSet is optimized for checking element membership and ensuring uniqueness. It's useful when you only need to store a collection of distinct elements.

### defaultdict() vs defaultdict(set) in python: : Main Differences
- `defaultdict()`: Defaultdict is a sub-class of the dictionary class that returns a dictionary-like object. The functionality of both dictionaries and defaultdict are almost same except for the fact that defaultdict never raises a KeyError. It provides a default value for the key that does not exists.

- `defaultdict(set)`: When you pass the set class as the default_factory argument when creating a defaultdict, it allows you to create a defaultdict where the default value for missing keys is an empty set (set()), and you can directly add values to these sets for each missing key. 

