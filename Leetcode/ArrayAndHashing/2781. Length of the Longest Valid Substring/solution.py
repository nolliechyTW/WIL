class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        # Convert the list of forbidden substrings to a set for efficient lookups.
        setF = set(forbidden)
        # Initialize the result (length of the longest valid substring) to 0.
        res = 0 
        # Initialize the left pointer of the sliding window.
        left = 0

        # Iterate through the string with the right pointer.
        for right in range(len(word)): 
            # Check substrings starting from the right pointer and going back up to 10 characters,
            # or to the left pointer, whichever is less.
            for i in range(right, max(left - 1, right - 10), -1):
                # If the current substring is in the set of forbidden substrings, move the left pointer
                # just after this forbidden substring and break the loop.
                if word[i : right + 1] in setF:
                    left = i + 1
                    break
            # Update the result with the maximum length found so far.
            res = max(res, right - left + 1)
        
        # Return the length of the longest valid substring.
        return res
