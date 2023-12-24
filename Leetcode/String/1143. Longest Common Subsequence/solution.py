class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 2d grid - dynamic programming, initializing with 0
        # top down 
        N = len(text1)
        M = len(text2)
        dp = [[0]*(M+1) for _ in range(N+1)]

        for i in range(N):
            for j in range(M):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        
        return dp[N][M]
