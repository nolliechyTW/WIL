class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert the wordDict into a set for faster lookup
        wordSet = set(wordDict)
        
        # Initialize the dp (dynamic programming) array where dp[i] is True if the 
        # substring s[:i] can be segmented into words in the wordDict
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Base case: an empty string can always be segmented

        # Loop through each character in the string 's'
        for i in range(1, len(s) + 1):
            # Try to match every word in the wordSet with the end of the substring s[:i]
            for word in wordSet:
                wordLen = len(word)  # Get the current word's length
                # Ensure two conditions:
                # 1. The current position i is at least as far into the string as the length of the word.
                #    This prevents negative indexing in the dp array.
                # 2. The substring ending at 'i' and is as long as the word matches the word itself.
                if i >= wordLen and dp[i - wordLen] and s[i - wordLen:i] == word:
                    dp[i] = True  # If both conditions are met, set dp[i] to True.
                    break  # No need to check further; break out of the loop for efficiency.

        # Return the last element in dp array which represents whether the whole string 
        # 's' can be segmented into a sequence of dictionary words.
        return dp[-1]

# alternative solution using dfs + memoization
# time complexity: O(n^2)
# space complexity: O(n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)  # Convert to set for O(1) lookups
        memo = {}  # Dictionary to remember results of previous calls

        def dfs(word):
            if word in memo:  # Check if result is already computed
                return memo[word]
            if word in wordSet:  # Base case for optimization
                memo[word] = True
                return True
            for i in range(1, len(word)):  # Start from 1 to avoid empty string
                prefix = word[:i]
                suffix = word[i:]
                if prefix in wordSet and (suffix in wordSet or dfs(suffix)):
                    memo[word] = True
                    return True
            memo[word] = False
            return False

        return dfs(s)
