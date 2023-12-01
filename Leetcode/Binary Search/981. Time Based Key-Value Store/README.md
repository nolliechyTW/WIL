## 981. Time Based Key-Value Store
🔗  Link: [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: HashTable, Binary Search, Design<br>

=======================================================================================<br>
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.<br>

Implement the `TimeMap` class:<br>

1) `TimeMap()` Initializes the object of the data structure
2) `void set(String key, String value, int timestamp)`:
Stores the `key` with the `value` at the given time timestamp
3) `String get(String key, int timestamp)`:
Returns a value such that `set` was called previously, with `timestamp_prev <= timestamp`. If there are multiple such values, it returns the value associated with the largest `timestamp_prev`. If there are no values, it returns `""`



Example 1:<br>

Input<br>
["TimeMap", "set", "get", "get", "set", "get", "get"]<br>
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]<br>
Output<br>
[null, null, "bar", "bar", null, "bar2", "bar2"]<br>

Explanation<br>
TimeMap timeMap = new TimeMap();<br>
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.<br>
timeMap.get("foo", 1);         // return "bar"<br>
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".<br>
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.<br>
timeMap.get("foo", 4);         // return "bar2"<br>
timeMap.get("foo", 5);         // return "bar2"<br>

Constraints:<br>
- 1 <= key.length, value.length <= 100
- key and value consist of lowercase English letters and digits.
- 1 <= timestamp <= 10^7
- At most 2 * 10^5 calls will be made to set and get.
=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Should the timestamps be unique for each set operation, or is it acceptable to have multiple set operations with the same timestamp for a given key?
    - All the timestamps `timestamp` of `set` are strictly increasing
2. Any requirement on time/space complexity? 
    - You must write a solution in O(logn) time complexity for `get` and O(1) time complexity for `set`


### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


1. Binary Search <br>
Binary search is an efficient method for locating an element in a sorted list. Leveraging the fact that timestamps are strictly increasing, binary search can be employed to replace linear search, thereby enhancing the time complexity to O(logn)

2. HashTable <br>
HashTable is the go-to choice for a key-value data structure in this scenario. Its constant-time average-case complexity for both insertion and retrieval makes it particularly suitable for handling dynamic datasets with frequent updates


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

- General Idea: Utilize a Hashtable to efficiently store key-value pairs, where each key maps to a list containing pairs of values and timestamps. The set method adds new entries to this structure in constant time, while the get method employs binary search within the timestamp-sorted list to efficiently retrieve the value associated with the key at the specified timestamp.


### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug

### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

<!-- -->
