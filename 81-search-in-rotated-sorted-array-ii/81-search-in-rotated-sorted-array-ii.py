class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums.sort()
        l = 0
        r = len(nums)-1
        mid_index = 0
        
        while(l<=r):
            mid_index = (l+r)//2
            mid_number = nums[mid_index]
            
            if mid_number == target:
                return True
            if mid_number<target:
                l = mid_index+1
            else:
                r = mid_index-1
        return False
        