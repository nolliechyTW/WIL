class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                if not stack or (char == ')' and stack[-1] != '(')  or (char == '}' and stack[-1] != '{') or (char == ']' and stack[-1] != '['):
                    return False
                stack.pop() # we find a pair
        
        return not stack # if stack is empty, return True, else return False
