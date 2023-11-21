class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # List to store the generated valid parenthesis combinations
        res = []
        # Stack to keep track of the current parenthesis sequence being formed
        stack = []
       
        def backtrack(open, close):
            # Base case: If the desired length is reached, add the generated sequence to the result
            if open == close == n:
                res.append("".join(stack))
                return
            
            # Try adding an opening parenthesis if the count is less than 'n'
            if open < n:
                stack.append("(")
                backtrack(open+1, close)
                stack.pop()  # Backtrack: Remove the last character to explore other possibilities
            
            # Try adding a closing parenthesis if the count is less than 'open'
            if close < open:
                stack.append(")")
                backtrack(open, close+1)
                stack.pop()  # Backtrack: Remove the last character to explore other possibilities
        
        # Start the backtracking process with initial counts of open and close parentheses
        backtrack(0, 0)
        # Return the list of valid parenthesis combinations
        return res
