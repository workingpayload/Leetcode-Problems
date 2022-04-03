class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        num = sum(nums) - sum(set(nums))
        n = len(nums)
        total_sum = n*(n+1)//2
        
        array_sum = total_sum - sum(nums)
        
        return [num,array_sum+num]
        