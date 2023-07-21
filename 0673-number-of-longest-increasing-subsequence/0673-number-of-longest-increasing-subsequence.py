class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*n
        count=[1]*n
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j]:
                    if 1+dp[j]>dp[i]:
                        dp[i]=dp[j]+1

                        count[i]=count[j]

                    elif dp[j]+1==dp[i]:
                        count[i]+=count[j]
        longest_len=max(dp)
        return sum([count[i] for i in range(n) if dp[i]==longest_len])   