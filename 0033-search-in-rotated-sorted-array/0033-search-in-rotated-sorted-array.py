class Solution:
    def search(self, nums: List[int], target: int) -> int:

        k = bisect_left(nums, True, key = lambda x: x < nums[0])  # <-- 1
 
        if target  >= nums[0]:                                    # <-- 2
            
            left = bisect_left(nums, target, hi = k-1)            # 
            return left if nums[left] == target else -1           #
                                                                  # <-- 3
        rght = bisect_left(nums, target, lo = k)                  #
        return rght if rght < len(nums                            # (this line to avoid index out of range)
                     ) and nums[rght] == target else -1           #