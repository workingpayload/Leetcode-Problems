class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        w1, w2 = len(word1), len(word2)
        
        @lru_cache(None)
        def dp(i, j):
            if i >= w1             : return w2-j                
            if j >= w2             : return w1-i                
            if word1[i] == word2[j]: return dp(i+1, j+1)        
            return min(dp(i,j+1), dp(i+1,j), dp(i+1,j+1)) + 1   

        return dp(0,0)