## 206. Reverse Linked List
🔗  Link: [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/description/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: Linked List, Recursion<br>

=======================================================================================<br>
You have a browser of one tab where you start on the `homepage` and you can visit another `url`, get back in the history number of `steps` or move forward in the history number of `steps`.<br>

Implement the `BrowserHistory` class:<br>

- `BrowserHistory(string homepage)` Initializes the object with the homepage of the browser.
- `void visit(string url)` Visits `url` from the current page. It clears up all the forward history.
- `string back(int steps)` Move steps back in history. If you can only return `x` steps in the history and `steps > x`, you will return only `x` steps. Return the current `url` after moving back in history at most steps.
- s`tring forward(int steps)` Move steps forward in history. If you can only forward `x` steps in the history and `steps > x`, you will forward only `x` steps. Return the current `url` after forwarding in history at most steps.

Example 1:<br>
Input: ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]<br>
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]<br>
Output: [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]<br>
Explaination: 
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");<br>
browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"<br>
browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"<br>
browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"<br>
browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"<br>
browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"<br>
browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"<br>
browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"<br>
browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.<br>
browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"<br>
browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"<br>



Constraints:<br>
- 1 <= homepage.length <= 20
- 1 <= url.length <= 20
- 1 <= steps <= 100
- `homepage` and `url` consist of  `'.'` or lower case English letters
- At most 5000 calls will be made to `visit`, `back`, and `forward`
=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input be empty? (head is null?)
    - Yes
2. Any requirement on time/space complexity?
    - O(N) in time and O(1) in space 
3. Does the linked list have a cycle?
    - No

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Doubly Linked List
- Linked lists are dynamic data structures, which means they can grow and shrink at runtime. This is particularly useful for browser history functionality, where the number of visited URLs is not known in advance and can change over time
- Adding or removing nodes (i.e., visiting a new URL or possibly deleting history) is relatively efficient. In the case of visiting a new URL, you only need to adjust the pointers of the current node and the new node, which is an O(1) operation
- Unlike arrays or dynamic arrays (like Python lists), linked lists do not require preallocating memory. Memory is allocated as needed for each new node, which can be more memory efficient, especially when the size of the history is unpredictable
- (cons) Each node in a linked list requires extra memory for its **pointers** (`next` and `pre` in the case of a doubly linked list), in addition to the actual data (URL). This overhead can make linked lists less memory efficient compared to arrays when the additional memory for pointers is significant relative to the data size


### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: leveraging the bidirectional links between nodes for quick access to adjacent entries


### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume `n` visit calls are made, `m` is the maximum number of steps to go forward or back, and `l` is the maximum length of a URL string.

- Time Complexity: O(min(n, m))
- Space Complexity: O(l⋅n) in worst case since we may visit n URL strings and they will be stored in our doubly linked list.
