# optimal solution
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Helper function to find the next valid character index
        # stops iterating and returns the "next valid index" when it finds a character that is not erased by a backspace.
        def find_next_valid_char_index(string, index):
            backspace_count = 0  
            while index >= 0:  # Iterates backwards through the string, until the start is reached
                if string[index] == '#':  # If the current character is a backspace character
                    backspace_count += 1  # Increment the count of backspace characters
                elif backspace_count > 0:  # If the current character is not a backspace, but we have previously encountered backspace(s)
                    backspace_count -= 1  # Decrement the backspace count, indicating a character is "deleted" by a backspace
                else:  # If the current character is not a backspace, and there are no backspaces to apply
                    break  # We've found a valid character that is not a backspace and not "deleted" by one, exit the loop
                index -= 1  # Move to the previous character to continue checking
            return index  # Returns the index of the found valid character, or -1 if none is found

        
        # Start from the end of both strings
        index1, index2 = len(s) - 1, len(t) - 1
        while index1 >= 0 or index2 >= 0:
            # Find the next valid character in both strings
            index1 = find_next_valid_char_index(s, index1)
            index2 = find_next_valid_char_index(t, index2)
            
            # If both strings are fully processed, they match
            if index1 < 0 and index2 < 0:
                return True
            
            # If only one string is fully processed, they don't match
            if index1 < 0 or index2 < 0 or s[index1] != t[index2]:
                return False
            
            # Move to the next character in both strings
            index1 -= 1
            index2 -= 1 
            
        return True




# brute force solution
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build_final_string(input_str: str) -> str:
            """Process the string to simulate backspace character removal."""
            final_str = []
            for char in input_str:
                if char != '#':
                    final_str.append(char)
                elif final_str:
                    final_str.pop()
            return ''.join(final_str)
        
        # Compare the processed versions of both strings.
        return build_final_string(s) == build_final_string(t)
