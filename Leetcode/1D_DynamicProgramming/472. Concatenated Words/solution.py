class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        setofWords = set(words)
        ans = []
        memo = defaultdict()  # Cache for memoization

        def dfs(word):
            if word in memo:  # Check if result is already computed
                return memo[word]
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in setofWords:
                    if suffix in setofWords or dfs(suffix):
                        memo[word] = True  # Cache the result
                        return True
            memo[word] = False  # Cache the result
            return False

        for word in words:
            if dfs(word):
                ans.append(word)
        return ans
