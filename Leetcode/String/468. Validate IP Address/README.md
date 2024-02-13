## 468. Validate IP Address
🔗  Link: [Validate IP Address](https://leetcode.com/problems/validate-ip-address/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: String<br>

=======================================================================================<br>

Given a string `queryIP`, return `"IPv4"` if IP is a valid IPv4 address, `"IPv6"` if IP is a valid IPv6 address or `"Neither"` if IP is not a correct IP of any type.

A valid **IPv4** address is an IP in the form "`x1.x2.x3.x4`" where `0 <= xi <= 255` and `xi` cannot contain leading zeros. For example, `"192.168.1.1"` and `"192.168.1.0"` are valid IPv4 addresses while `"192.168.01.1"`, `"192.168.1.00"`, and `"192.168@1.1"` are invalid IPv4 addresses.

A valid **IPv6** address is an IP in the form `"x1:x2:x3:x4:x5:x6:x7:x8"` where:
- 1 <= xi.length <= 4
- xi is a hexadecimal string which may contain digits, lowercase English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
- Leading zeros are allowed in xi.<br>

For example, `"2001:0db8:85a3:0000:0000:8a2e:0370:7334"` and `"2001:db8:85a3:0:0:8A2E:0370:7334"` are valid IPv6 addresses, while `"2001:0db8:85a3::8A2E:037j:7334"` and `"02001:0db8:85a3:0000:0000:8a2e:0370:7334"` are invalid IPv6 addresses.


Example 1:<br>
Input: queryIP = "172.16.254.1"<br>
Output: "IPv4"<br>
Explanation: This is a valid IPv4 address, return "IPv4".<br>


Example 2:<br>
Input: queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"<br>
Output: "IPv6"<br>
Explanation: This is a valid IPv6 address, return "IPv6".<br>

Example 3:<br>
Input: queryIP = "256.256.256.256"<br>
Output: "Neither"<br>
Explanation: This is neither a IPv4 address nor a IPv6 address.<br>

Constraints:<br>
- queryIP consists only of `English letters`, `digits` and the characters `'.'` and `':'`.<br>


=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1.  Any requirement on time/space complexity?
- O(n) in time complexity and O(1) in space complexity
2. Can you confirm the range of characters that the input string might contain? Are we considering just ASCII characters, or should the solution also handle Unicode characters (which might include emojis, symbols, etc.)?
- `s` consists only of printable ASCII characters.
3. Are there any specific edge cases you'd like the solution to handle? For example, empty strings, strings with only one character, or strings with only non-alphanumeric characters?
- you should handle all of them 

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category


- Two pointers<br>
Since we got a hint that this question should be solved in O(1) space complexity, instead of using string manipulation or array to brute force the problem, we can simply use two pointers to neglect characters that are not valid. This approach allows us to evaluate the palindrome property in place, without the need for additional data structures.

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: With two pointers, one at the beginning and one at the end of the string, we can compare the characters these pointers refer to. If both characters are alphanumeric and identical (considering case insensitivity), we move the pointers closer to the center of the string, continuing this process. Whenever we encounter non-alphanumeric characters, we can skip them by moving the respective pointer inwards. This way, we efficiently ignore invalid characters and focus only on the parts of the string that matter for palindrome validation.<br>

1) Initialize Pointers
- Start with two pointers, `left` at the beginning and `right` at the end of the string.
2) Traverse String with Pointers
- Use a `while` loop to move `left` and `right` towards each other, stopping when they meet or cross.
3) Skip Non-Alphanumeric Characters
- Inside the loop, increment `left` and decrement `right` to skip over any non-alphanumeric characters.
4) Character Comparison
- Compare the characters at `left` and `right` indices, considering case insensitivity. If they don't match, return `False`.
5) Move Pointers and Repeat
- If characters match, move `left` one step right and `right` one step left, then repeat the comparison.
6) Complete Check
- If the loop completes without mismatches, return `True`, indicating the string is a palindrome.

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N is the length of the string `s`.

- Time Complexity: O(N)
- Space Complexity: O(1)