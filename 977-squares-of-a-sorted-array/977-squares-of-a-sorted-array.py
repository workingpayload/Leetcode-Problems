class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = n-1
        index = n-1
        result = [0 for i in range(n)]
        
        while index>=0:
            if abs(nums[left])>=abs(nums[right]):
                result[index]=nums[left]*nums[left]
                left+=1
            else:
                result[index]=nums[right]*nums[right]
                right-=1
            index-=1
            
        return result    
                