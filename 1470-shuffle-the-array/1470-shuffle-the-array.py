class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums2 = []
        mid = len(nums)//2
        
        mid1=mid
        
        for i in range(mid):
            nums2.append(nums[i])
            nums2.append(nums[mid1])
            mid1+=1
            
            
        return nums2    
            