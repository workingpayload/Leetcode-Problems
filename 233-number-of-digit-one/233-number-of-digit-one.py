class Solution:
    def countDigitOne(self, n: int) -> int:
        s = str(n)
        dp = [[[0,0] for i in range(10)] for i in range(len(s))]
        ans = 0
        extra_ones = 1

        flag = -1
        next_flag = -1
        for i in range(0,len(s)):
            for j in range(0,10):
                if(j==1):
                    dp[i][j][0] = extra_ones
                if(i==0):
                    dp[i][j][0] += dp[i][j-1][0]

                else:
                    dp[i][j][0] += dp[i-1][9][0] + dp[i][j-1][0]

                if(j == int(s[len(s)-i-1])):
                    dp[i][j][1] = dp[i][j-1][0] + dp[i-1][flag][1]
                    if(j==1):
                        if(i==0):
                            dp[i][j][1]+=1
                        else:
                            dp[i][j][1]+= int(s[len(s)-i:])+1
                    flag = j
            extra_ones*=10
        return dp[-1][flag][1]