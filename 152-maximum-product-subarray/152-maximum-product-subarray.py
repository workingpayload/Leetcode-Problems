class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        dp = [0]*len(nums)
        dm = [0]*len(nums)
        dp[0]=nums[0]
        dm[0]=nums[0]
        
        for i in range(1,len(nums)):
            dp[i]=max(dp[i-1]*nums[i],dm[i-1]*nums[i],nums[i])
            dm[i]=min(dp[i-1]*nums[i],dm[i-1]*nums[i],nums[i])
            
        return max(dp)    