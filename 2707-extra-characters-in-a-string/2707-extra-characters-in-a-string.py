class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        n,dp = len(s),[0]
        max_word_len = len(max(dictionary, key=len))
        for i in range(1,n+1):
            dp.append(dp[-1]+1)
            for j in range(i-1,max(i-max_word_len-1,-1),-1):
                if s[j:i] in dictionary:
                    dp[i] = min(dp[i],dp[j])
        return dp[-1]