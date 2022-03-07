class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        mid = 0
        while(l<=r):
            mid = (l+r)//2
            mid_no = nums[mid]
            if mid_no==target:
                    return mid
            elif mid_no<target:
                  l = mid + 1
            else:
                  r = mid - 1
        if mid_no>target:
                return l
        else:
                return r+1