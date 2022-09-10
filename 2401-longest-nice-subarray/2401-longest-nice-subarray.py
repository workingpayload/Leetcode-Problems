class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        andSubArray, ans, j = 0, 0, 0
        for i in range(len(nums)):
            while andSubArray & nums[i]:
                andSubArray ^= nums[j]
                j += 1
            andSubArray |= nums[i]
            ans = max(ans, i - j + 1)
        return ans