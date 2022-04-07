class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum1 = [nums[0]]
        
        for i in range(1,len(nums)):
            sum1.append(sum(nums[:i])+nums[i])
            
            
        return sum1    