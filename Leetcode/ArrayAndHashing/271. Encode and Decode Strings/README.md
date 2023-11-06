## 271. Encode and Decode Strings
🔗  Link: [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array, String, Design<br>

=======================================================================================<br>
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.<br>

Machine 1 (sender) has the function:<br>
```
        string encode(vector<string> strs) {
        // ... your code
        return encoded_string;
        }
```

Machine 2 (receiver) has the function:<br>
```
        vector<string> decode(string s) {
        //... your code
        return strs;
        }
```

So Machine 1 does:<br>
`string encoded_string = encode(strs);`<br>

and Machine 2 does:<br>
`vector<string> strs2 = decode(encoded_string)`;<br>
strs2 in Machine 2 should be the same as strs in Machine 1.<br>

Implement the encode and decode methods.<br>

You are not allowed to solve the problem using any serialize methods (such as eval).<br>

Example 1:<br>
Input: dummy_input = ["Hello","World"]<br>
Output: ["Hello","World"]<br>
Explanation:<br>
- Machine 1:<br>
Codec encoder = new Codec();<br>
String msg = encoder.encode(strs);<br>
Machine 1 ---msg---> Machine 2<br>

- Machine 2:<br>
Codec decoder = new Codec();<br>
String[] strs = decoder.decode(msg);<br>


Example 2:<br>
Input: dummy_input = [""]<br>
Output: [""]<br>

Constraints:<br>
1 <= strs.length <= 200<br>
0 <= strs[i].length <= 200<br>
strs[i] contains any possible characters out of 256 valid ASCII characters.<br>
=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the input be empty?
2. Any requirement on time/space complexity?
3. Will the input only contains ASCII character?

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

- String Manipulation<br>
The problem involves handling strings in various ways, such as replacing characters, splitting strings, and building new strings based on specific rules. In this case, the encoding function manipulates the input list of strings to create a single encoded string, while the decoding function processes the encoded string to reconstruct the original list of strings.

- Escaping<br>
Escaping is a common concept in computer programming. By choosing a specific character to act as an "escape character", we can denote that any special character following the escape character should be treated as a normal character instead of its special meaning. It's popular to use the slash character `/` as our escape character.

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Choose a special delimeter that can help us recognize the breakpoint between each input and therefore implementing encode and decode method.

1) In the encode method, iterate through each string in the input list, replace '/' with '//', and add '/:' to the end of each string. Combine all these encoded strings into a single string, separating them by '/:'.
2) In the decode method, iterate through the encoded string and rebuild the original list of strings. Handle escaped slashes ('//') and the delimiter '/:' to split the encoded string back into individual strings.


### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Let `n` denote the total number of characters across all strings in the input list and `k` denote the number of strings.

- Time Complexity: O(n)
Both encoding and decoding processes iterate over every character in the input, thus they both have a linear time complexity of O(n)

- Space Complexity: O(k)
We don't count the output as part of the space complexity, but for each word, we are using some space for the escape character and delimiter