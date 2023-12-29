class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 2d grid - dynamic programming, initializing with 0
        # top down 
        N = len(text1)
        M = len(text2)
        # The extra row and column (thus N+1 and M+1) are used to 
        # handle edge cases where one or both strings are empty.
        dp = [[0]*(M+1) for _ in range(N+1)]

        for i in range(N):
            for j in range(M):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        
        for row in dp: # for testing
            print(row)
            
        return dp[N][M]


# Test case
sol = Solution()
text1 = "abcde"
text2 = "ace"
print("Length of Longest Common Subsequence:", sol.longestCommonSubsequence(text1, text2))


# [0, 0, 0, 0]
# [0, 1, 1, 1]
# [0, 1, 1, 1]
# [0, 1, 2, 2]
# [0, 1, 2, 2]
# [0, 1, 2, 3]
# Length of Longest Common Subsequence: 3
